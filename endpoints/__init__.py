from fastapi import FastAPI
from db import Session

app = FastAPI()
session = Session()
