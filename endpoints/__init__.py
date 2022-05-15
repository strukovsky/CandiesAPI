import os

from fastapi import FastAPI
from db import Session

app = FastAPI()
session = Session()
HOST = os.environ.get("HOST", "http://127.0.0.1")
PORT = os.environ.get("PORT", "8000")


@app.get("/")
def root():
    return {
        "users": f"{HOST}:{PORT}/users/",
        "chupachupses": f"{HOST}:{PORT}/chupachupses/",
    }
