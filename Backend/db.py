from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import PickleType
import cv2

import base64

DATABASE_URL = "sqlite:///./db.db?check_same_thread=False"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = "users"
    oauth_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=True)
    favourite_recipes = Column(PickleType)
    owned_recipes = Column(PickleType)

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    instructions = Column(String)
    ingredients = Column(PickleType)
    image64 = Column(PickleType)

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    recipes = Column(PickleType)

def image_to_base64(image,binary_mode=False):
    if binary_mode:
        cv2.imwrite("temp.jpg", image)
        image = "temp.jpg"
    with open(image, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    from db_filler import fill_db
    fill_db()