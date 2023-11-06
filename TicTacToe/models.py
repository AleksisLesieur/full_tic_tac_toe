# from database import Base
# from sqlalchemy import Column, Integer, String

# class TicTacToe(Base):
#     __tablename__ = 'TicTacToe'

#     id = Column(Integer, primary_key=True, index=True)
#     cell_1_1 = Column(String(1), nullable=True)  # Top-Left
#     cell_1_2 = Column(String(1), nullable=True)  # Top-Center
#     cell_1_3 = Column(String(1), nullable=True)  # Top-Right
#     cell_2_1 = Column(String(1), nullable=True)  # Middle-Left
#     cell_2_2 = Column(String(1), nullable=True)  # Middle-Center
#     cell_2_3 = Column(String(1), nullable=True)  # Middle-Right
#     cell_3_1 = Column(String(1), nullable=True)  # Bottom-Left
#     cell_3_2 = Column(String(1), nullable=True)  # Bottom-Center
#     cell_3_3 = Column(String(1), nullable=True)  # Bottom-Right