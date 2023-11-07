from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
# from database import engine, SessionLocal
# import models
# from models import TicTacToe
# from sqlalchemy.orm import Session


from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")

class BoxData(BaseModel):
    box1: Optional[str] = None
    box2: Optional[str] = None
    box3: Optional[str] = None
    box4: Optional[str] = None
    box5: Optional[str] = None
    box6: Optional[str] = None
    box7: Optional[str] = None
    box8: Optional[str] = None
    box9: Optional[str] = None

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse('index_refactored.html', {"request": request})

@app.post("/")
async def receive_data(box_data: BoxData):
    return box_data

# added code


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/game/")
# async def create_game(box_data: BoxData, db: Session = Depends(get_db)):
#     db_game = TicTacToe(
#         cell_1_1=box_data.box1, 
#         cell_1_2=box_data.box2,
#         cell_1_3=box_data.box3, 
#         cell_1_4=box_data.box4,
#         cell_1_5=box_data.box5, 
#         cell_1_6=box_data.box6,
#         cell_1_7=box_data.box7, 
#         cell_1_8=box_data.box8,
#         cell_1_9=box_data.box9, 
#     )
#     db.add(db_game)
#     db.commit()
#     db.refresh(db_game)
#     return db_game


