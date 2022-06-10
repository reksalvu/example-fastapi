#FastAPI, HTTPExeption/status -> http status code 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


#pyscopg2 -> PostgreSQL database adapter for the Python 

#pydantic, schema and data validations
from .config import settings

#sqlalchemy

#import file
from . import models
from .database import engine
from .routers import post, user, auth, vote


#create all the models.py
#models.Base.metadata.create_all(bind=engine)

app = FastAPI() #FastAPI (app) instance

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") #@app decorator, path operation
def root():
    return {"message": "Hello!!!"}




