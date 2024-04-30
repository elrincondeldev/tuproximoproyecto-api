from sqlalchemy.orm import Session
from api.models.project import Project
from api.schemas.project import ProjectBase
from typing import List
from datetime import datetime

def create_project(db: Session, project: ProjectBase):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    projects = db.query(Project).offset(offset).limit(page_size).all()
    projects_data = [project.serialize() for project in projects]
    total_projects = db.query(Project).count()
    total_pages = total_projects // page_size
    return projects_data, total_pages

def get_today_projects(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    projects = db.query(Project).filter(Project.created_at == datetime.now().date()).offset(offset).limit(page_size).all()
    projects_data = [project.serialize() for project in projects]
    total_projects = db.query(Project).filter(Project.created_at == datetime.now().date()).count()
    total_pages = total_projects // page_size
    return projects_data, total_pages

def get_frontend_projects(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    projects = db.query(Project).filter(Project.category == "frontend").offset(offset).limit(page_size).all()
    projects_data = [project.serialize() for project in projects]
    total_projects = db.query(Project).filter(Project.category == "frontend").count()
    total_pages = total_projects // page_size
    return projects_data, total_pages

def get_backend_projects(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    projects = db.query(Project).filter(Project.category == "backend").offset(offset).limit(page_size).all()
    projects_data = [project.serialize() for project in projects]
    total_projects = db.query(Project).filter(Project.category == "backend").count()
    total_pages = total_projects // page_size
    return projects_data, total_pages

def get_fullstack_projects(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    projects = db.query(Project).filter(Project.category == "fullstack").offset(offset).limit(page_size).all()
    projects_data = [project.serialize() for project in projects]
    total_projects = db.query(Project).filter(Project.category == "fullstack").count()
    total_pages = total_projects // page_size
    return projects_data, total_pages

def get_projects_names(db: Session) -> List[str]:
    projects_names = db.query(Project.name).all()
    projects_names_list = [name[0] for name in projects_names]
    return projects_names_list

def search_projects_by_name(db: Session, search_query: str) -> List[Project]:
    projects = db.query(Project).filter(Project.name.ilike(f"%{search_query}%")).all()
    print(projects)
    return projects