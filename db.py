from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)


class ChupaChups(Base):
    __tablename__ = "chupachupses"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    diameter = Column(Integer)
    flavor = Column(String)
    stick_size = Column(Integer)


Base.metadata.create_all()
