from db import ChupaChups
from endpoints import app, session
from models import ChupaChupsModel


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
