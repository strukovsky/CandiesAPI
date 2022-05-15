from fastapi import FastAPI
from db import User, Session, ChupaChups
from models import UserModel, ChupaChupsModel

app = FastAPI()
session = Session()


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


@app.get("/chupachupses/")
async def get_all_chupachupses():
    return {
        "chupachupses": session.query(ChupaChups).all()
    }


@app.get("/chupachupses/{_id}/")
async def get_specific_chupachups(_id: int):
    return {str(_id): session.query(ChupaChups).get(_id)}


@app.post("/chupachupses/")
async def create_new_chupachups(chupachups: ChupaChupsModel):
    session.add(ChupaChups(**chupachups.dict()))
    session.commit()
