from pydantic import BaseModel


class UserModel(BaseModel):
    username: str


class ChupaChupsModel(BaseModel):
    diameter: int
    flavor: str
    stick_size: int
