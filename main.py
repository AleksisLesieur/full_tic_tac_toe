from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated, Optional

# database imports

from database import engine, SessionLocal
import models
from models import TicTacToe
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class BoxData(BaseModel):
    cell_1_1: Optional[str] = None
    cell_1_2: Optional[str] = None
    cell_1_3: Optional[str] = None
    cell_2_1: Optional[str] = None
    cell_2_2: Optional[str] = None
    cell_2_3: Optional[str] = None
    cell_3_1: Optional[str] = None
    cell_3_2: Optional[str] = None
    cell_3_3: Optional[str] = None

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse('index_refactored.html', {"request": request})

# @app.post("/")
# async def receive_data(box_data: BoxData):
#     return box_data

# added code


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/game")
async def create_game(box_data: BoxData, db: db_dependency):
    print(f"Received box data: {box_data}")  
    db_game = models.TicTacToe(
        cell_1_1 = box_data.cell_1_1, 
        cell_1_2 = box_data.cell_1_2,
        cell_1_3 = box_data.cell_1_3, 
        cell_2_1 = box_data.cell_2_1,
        cell_2_2 = box_data.cell_2_2, 
        cell_2_3 = box_data.cell_2_3,
        cell_3_1 = box_data.cell_3_1, 
        cell_3_2 = box_data.cell_3_2,
        cell_3_3 = box_data.cell_3_3,
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    print(f"Game saved with ID {db_game.id} and data: {db_game}")
    return db_game

@app.put("/game/{game_id}")
async def update_game(game_id: int, box_data: BoxData, db: db_dependency):
    db_game = db.query(models.TicTacToe).filter(models.TicTacToe.id == game_id).first()
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    
    # Update the fields
    db_game.cell_1_1 = box_data.cell_1_1 or db_game.cell_1_1
    db_game.cell_1_2 = box_data.cell_1_2 or db_game.cell_1_2
    db_game.cell_1_3 = box_data.cell_1_3 or db_game.cell_1_3
    db_game.cell_2_1 = box_data.cell_2_1 or db_game.cell_2_1
    db_game.cell_2_2 = box_data.cell_2_2 or db_game.cell_2_2
    db_game.cell_2_3 = box_data.cell_2_3 or db_game.cell_2_3
    db_game.cell_3_1 = box_data.cell_3_1 or db_game.cell_3_1
    db_game.cell_3_2 = box_data.cell_3_2 or db_game.cell_3_2
    db_game.cell_3_3 = box_data.cell_3_3 or db_game.cell_3_3
    
    db.commit()
    db.refresh(db_game)
    return db_game


