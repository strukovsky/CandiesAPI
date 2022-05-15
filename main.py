from fastapi import FastAPI
from db import User, Session
from models import UserModel

app = FastAPI()
session = Session()


@app.get("/users/")
async def get_all_users():
    return {
        "users": session.query(User).all()}


@app.get("/users/{username}/")
async def get_specific_user(username: str):
    return {username: session.query(User).filter(User.username == username).first()}


@app.post("/users/")
async def create_new_user(user: UserModel):
    user_to_db = User(**user.dict())
    session.add(user_to_db)
    session.commit()
