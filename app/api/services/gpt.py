from openai import OpenAI
from dotenv import load_dotenv
import json
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import os
from api.services import project as project_service
from sqlalchemy.orm import Session
from api.schemas.project import ProjectBaseGpt
from datetime import datetime, timezone, timedelta
from api.auth import security as verify_token
import pytz

load_dotenv()

API_KEY = os.getenv("GPT_KEY")

client = OpenAI(api_key=API_KEY)

app = FastAPI()

class Project(BaseModel):
    name: str
    description: str
    votes: int
    category: str
    type: bool
    created_at: datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
    
async def generate_project_idea(db: Session, token: dict = Depends(verify_token.verify_token)):
    spain_tz = pytz.timezone('Europe/Madrid')

    current_datetime = datetime.now(spain_tz)

    current_datetime_isoformat = current_datetime.isoformat()

    projectsNames = project_service.get_projects_names(db)

    projects_list = "\n".join([f"- {name}" for name in projectsNames])

    prompt = f"""
    Genera una idea para un proyecto de programación que cumpla con los siguientes criterios:
    - name: Un nombre descriptivo para el proyecto.
    - description: Una breve descripción del proyecto.
    - votes: 0
    - category: Debe ser automáticamente asignado entre "frontend", "backend" o "fullstack".
    - type: true

    Recuerda que el proyecto debe ser frontend, backend o fullstack, las probabilidades de que salga cualquiera de los 3 deben ser iguales, en función de ello, la categoría será "frontend", "backend" o "fullstack".

    Recuerda que tanto el nombre como la descripción deben estar en español.

    Proyectos existentes:
    {projects_list}

    Ejemplo:
    {{
      "name": "",
      "description": "",
      "votes": 0,
      "category": "",
      "type": true,
      "created_at": "{current_datetime_isoformat}"
    }}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=0.9,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    project_data = json.loads(response.choices[0].message.content)

    project = ProjectBaseGpt(**project_data)

    project_service.create_project(db, project)
    
    return project_data
