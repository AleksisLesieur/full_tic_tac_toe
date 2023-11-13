from fastapi import FastAPI, Request, Depends, HTTPException, Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated, Optional
from starlette import status

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
    cell_1_4: Optional[str] = None
    cell_1_5: Optional[str] = None
    cell_1_6: Optional[str] = None
    cell_1_7: Optional[str] = None
    cell_1_8: Optional[str] = None
    cell_1_9: Optional[str] = None

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse('index_refactored.html', {"request": request})


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/received")
async def read_games(db: db_dependency):
    games = db.query(models.TicTacToe).all()
    return games

@app.get("/received/{game_id}", status_code=status.HTTP_200_OK)
async def receive_game(db: db_dependency, game_id: int = Path(gt=0)):
    game_data = db.query(models.TicTacToe).filter(models.TicTacToe.id == game_id).first()
    if game_data is not None:
        return game_data
    raise HTTPException(status_code=404, detail='Todo not found.')

@app.post("/game")
async def create_game(box_data: BoxData, db: db_dependency):
    print(f"Received box data: {box_data}")  
    db_game = models.TicTacToe(
        cell_1_1 = box_data.cell_1_1, 
        cell_1_2 = box_data.cell_1_2,
        cell_1_3 = box_data.cell_1_3, 
        cell_1_4 = box_data.cell_1_4,
        cell_1_5 = box_data.cell_1_5, 
        cell_1_6 = box_data.cell_1_6,
        cell_1_7 = box_data.cell_1_7, 
        cell_1_8 = box_data.cell_1_8,
        cell_1_9 = box_data.cell_1_9,
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
    db_game.cell_1_4 = box_data.cell_1_4 or db_game.cell_1_4
    db_game.cell_1_5 = box_data.cell_1_5 or db_game.cell_1_5
    db_game.cell_1_6 = box_data.cell_1_6 or db_game.cell_1_6
    db_game.cell_1_7 = box_data.cell_1_7 or db_game.cell_1_7
    db_game.cell_1_8 = box_data.cell_1_8 or db_game.cell_1_8
    db_game.cell_1_9 = box_data.cell_1_9 or db_game.cell_1_9
    
    db.commit()
    db.refresh(db_game)
    return db_game

