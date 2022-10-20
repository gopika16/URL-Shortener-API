import validators
from fastapi import FastAPI, HTTPException, Depends
import secrets
from sqlalchemy.orm import Session
from . import schemas,models
from .database import SessionLocal, engine

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# path operation decorator to associate root path with
# read_root() ...now FastAPI will listens to root path n
# will delegate all incoming GET REQ to 
# this function 
@app.get("/")
def read_root():
    return "Heyyyy! WELcome to URL shortner API :P "

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
    return db_url

# @app.post("/url")
# def create_url(url: schemas.URLBase):
#     if not validators.url(url.target_url):
#         raise_bad_request(message="Your provided URL is not valid")
#     return f"TODO: Create database entry for: {url.target_url}"


# python -m uvicorn shortener_app.main:app --reload 
# The --reload flag makes sure that your server will
#  reload automatically when you save your application’s code. 