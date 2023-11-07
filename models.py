from sqlalchemy import Column, Integer, String, Row
from database import Base

class TicTacToe(Base):
    __tablename__ = 'TicTacToe'

    id = Column(Integer, primary_key=True, index=True)
    cell_1_1 = Column(String, nullable=True, default=None)  # Top-Left
    cell_1_2 = Column(String, nullable=True, default=None)  # Top-Center
    cell_1_3 = Column(String, nullable=True, default=None)  # Top-Right
    cell_2_1 = Column(String, nullable=True, default=None)  # Middle-Left
    cell_2_2 = Column(String, nullable=True, default=None)  # Middle-Center
    cell_2_3 = Column(String, nullable=True, default=None)  # Middle-Right
    cell_3_1 = Column(String, nullable=True, default=None)  # Bottom-Left
    cell_3_2 = Column(String, nullable=True, default=None)  # Bottom-Center
    cell_3_3 = Column(String, nullable=True, default=None)  # Bottom-Right
