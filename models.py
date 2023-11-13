from sqlalchemy import Column, Integer, String
from database import Base

class TicTacToe(Base):
    __tablename__ = 'TicTacToe'

    id = Column(Integer, primary_key=True, index=True)
    cell_1_1 = Column(String, nullable=True, default=None)  # Top-Left
    cell_1_2 = Column(String, nullable=True, default=None)  # Top-Center
    cell_1_3 = Column(String, nullable=True, default=None)  # Top-Right
    cell_1_4 = Column(String, nullable=True, default=None)  # Middle-Left
    cell_1_5 = Column(String, nullable=True, default=None)  # Middle-Center
    cell_1_6 = Column(String, nullable=True, default=None)  # Middle-Right
    cell_1_7 = Column(String, nullable=True, default=None)  # Bottom-Left
    cell_1_8 = Column(String, nullable=True, default=None)  # Bottom-Center
    cell_1_9 = Column(String, nullable=True, default=None)  # Bottom-Right
