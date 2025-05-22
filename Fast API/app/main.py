from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return{"message" : "Happy Corgi!"}

# Notes

# New virtual enviornment
# py -3 -m venv venv

# Activate virtual environment in terminal
# venv\Scripts\activate.bat

# Execute web server that monitors for code changes
# uvicorn app.main:app --reload

"""
Version with params and Body, for post/createpost

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

"""

"""
# First example to store in memory

my_posts = [
    {"title": "Best videogames ever", "content": "Most popular videogames", "id": 1},
    {"title": "Worst videogames ever", "content": "Worst rated videogames", "id": 2}
    ]

# Function when working locally without database

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
           return post
        
def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i
"""