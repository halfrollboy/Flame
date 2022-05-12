from typing import List
from os import environ
from fastapi import HTTPException
from fastapi.params import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.models.pydantic.user import UserCreate

from ..models.postgres.pg_models import User
from ..db.postgres.dependencies import get_db
from ..models.pydantic.company import User

from passlib.context import CryptContext
from loguru import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db  # внедрение зависимостей

    def find(self, id: int) -> User:
        """Поиск пользователя по id"""
        query = self.db.query(User)
        return query.filter(User.id == id).first()

    # TODO Переделать запросы
    def find_by_username(self, username: int) -> User:
        """Поиск пользователя по id"""
        query = self.db.query(User).filter_by(username == username).first()
        return query

    def find_by_email(self, email: EmailStr):
        """Поиск ползователя по email"""
        query = self.db.query(User)
        return query.filter(User.email == email).first()

    # def all(self, skip: int = 0, max: int = 100) -> List[User]:
    #     """Получить всех пользователей"""
    #     query = self.db.query(User)
    #     return query.offset(skip).limit(max).all()