from sqlalchemy import Column, String, Integer, Boolean
from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)


    def __repr__(self):
        return f"Users [id={self.id}, name={self.name}, username={self.username}]"