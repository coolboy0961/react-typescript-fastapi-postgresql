from fastapi import Depends
from sqlalchemy.orm import Session
from src.interface.gateways.repositories.models.UserModel import UserModel
from src.infrastructure.database import get_db
from src.domain.entities.UserEntity import UserEntity


class UserRepository:
    def add(self, user: UserEntity, db: Session = Depends(get_db)) -> None:
        db_user = UserModel(id=user.id, name=user.name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
