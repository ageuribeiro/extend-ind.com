from sqlalchemy import Column, String, Integer, Boolean
from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    senha = Column(String(50), nullable=False)
    profile = Column(String(7), nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"Users [id={self.id}, name={self.name}, username={self.username}]"