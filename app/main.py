from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flutter Glossary API", description="A simple Flutter Glossary API built with FastAPI", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Glossary API. Go to /docs for documentation."}

@app.get("/terms/", response_model=list[schemas.Term])
def get_all_terms(db: Session = Depends(get_db)):
    return crud.get_terms(db)

@app.get("/terms/{term_name}", response_model=schemas.Term)
def get_term(term_name: str, db: Session = Depends(get_db)):
    term = crud.get_term_by_name(db, term_name)
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

@app.post("/terms/", response_model=schemas.Term)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    return crud.create_term(db, term)

@app.put("/terms/{term_name}", response_model=schemas.Term)
def update_term(term_name: str, term: schemas.TermUpdate, db: Session = Depends(get_db)):
    db_term = crud.update_term(db, term_name, term)
    if not db_term:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

@app.delete("/terms/{term_name}", response_model=schemas.Term)
def delete_term(term_name: str, db: Session = Depends(get_db)):
    db_term = crud.delete_term(db, term_name)
    if not db_term:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term
