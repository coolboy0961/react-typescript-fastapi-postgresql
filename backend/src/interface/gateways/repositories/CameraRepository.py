from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.entities.CameraEntity import CameraEntity
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.CameraModel import CameraModel
from src.domain.entities.UserEntity import UserEntity


class CameraRepository:
    def add(self, camera: CameraEntity, user: UserEntity, db: Session = Depends(get_db)) -> None:
        db_camera = CameraModel(id=camera.id, user_id=user.id)
        db.add(db_camera)
        db.commit()
        db.refresh(db_camera)
