from db import User
from endpoints import app, session
from models import UserModel


@app.get("/users/")
async def get_all_users():
    return {
        "users": session.query(User).all()
    }


@app.get("/users/{username}/")
async def get_specific_user(username: str):
    return {username: session.query(User).filter(User.username == username).first()}


@app.post("/users/")
async def create_new_user(user: UserModel):
    session.add(User(**user.dict()))
    session.commit()
