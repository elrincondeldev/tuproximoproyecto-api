from fastapi import FastAPI, Request, HTTPException, APIRouter, Depends
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

router = APIRouter()

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave pública de las variables de entorno
PUBLIC_KEY_PEM = os.getenv("CLERK_PUBLIC_KEY")

# Middleware para verificar el token JWT
async def authenticate(request: Request):
    # Obtener el token de sesión desde la cookie o el encabezado
    session_token = request.cookies.get("__session", "")
    if not session_token:
        session_token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if not session_token:
        raise HTTPException(status_code=401, detail="No se encontró el token de sesión")

    # Verificar el token
    try:
        decoded_token = jwt.decode(session_token, PUBLIC_KEY_PEM, algorithms=["RS256"])
        return decoded_token
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Token de sesión inválido")
