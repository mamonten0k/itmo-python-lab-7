from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app import models, schemas

def get_terms(db: Session):
    return db.query(models.Term).all()

def get_term_by_name(db: Session, name: str):
    return db.query(models.Term).filter(models.Term.name == name).first()

def create_term(db: Session, term: schemas.TermCreate):
    db_term = models.Term(name=term.name, description=term.description)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

def update_term(db: Session, name: str, term: schemas.TermUpdate):
    db_term = get_term_by_name(db, name)
    if not db_term:
        return None
    db_term.description = term.description
    db.commit()
    db.refresh(db_term)
    return db_term

def delete_term(db: Session, name: str):
    db_term = get_term_by_name(db, name)
    if not db_term:
        return None
    db.delete(db_term)
    db.commit()
    return db_term
