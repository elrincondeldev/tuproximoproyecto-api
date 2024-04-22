from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api.routes import projects
from api.routes import gpt_api
from api.routes import newsletter
from api.routes import proposedProjects
from db.database import engine, Base
from api.auth import token

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Configurar el middleware para desactivar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(gpt_api.router, prefix="/gpt", tags=["gpt"])
app.include_router(newsletter.router, prefix="/newsletter", tags=["newsletter"])
app.include_router(proposedProjects.router, prefix="/proposed-projects", tags=["proposed-projects"])
app.include_router(token.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
