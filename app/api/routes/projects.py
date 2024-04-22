from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas import project
from api.services import project as project_service
from db.database import get_db
from fastapi import Query

router = APIRouter()

@router.post("/create-project", response_model=project.ProjectBase)
def create_project(project: project.ProjectBase, db: Session = Depends(get_db)):
    return project_service.create_project(db, project)

@router.get("/get-projects", response_model=list[project.ProjectBase])
def get_projects(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), db: Session = Depends(get_db)):
    projects = project_service.get_projects(db, page, page_size)
    return projects

@router.get("/get-frontend-projects", response_model=list[project.ProjectBase])
def get_frontend_projects(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), db: Session = Depends(get_db)):
    projects = project_service.get_frontend_projects(db, page, page_size)
    return projects

@router.get("/get-backend-projects", response_model=list[project.ProjectBase])
def get_backend_projects(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), db: Session = Depends(get_db)):
    projects = project_service.get_backend_projects(db, page, page_size)
    return projects

@router.get("/get-fullstack-projects", response_model=list[project.ProjectBase])
def get_fullstack_projects(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1), db: Session = Depends(get_db)):
    projects = project_service.get_fullstack_projects(db, page, page_size)
    return projects

@router.get("/get-projects-names", response_model=list[str])
def get_projects_names(db: Session = Depends(get_db)):
    return project_service.get_projects_names(db)

@router.get("/search-projects-by-name", response_model=list[project.ProjectBase])
def search_projects_by_name(search_query: str, db: Session = Depends(get_db)):
    print(search_query)
    return project_service.search_projects_by_name(db, search_query)