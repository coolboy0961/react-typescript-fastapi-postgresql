from typing import List
from src.domain.entities.camera_entity import CameraEntity
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.camera_model import CameraModel
from src.domain.entities.user_entity import UserEntity


class CameraRepository:
    def add(self, cameras: CameraEntity, user: UserEntity) -> None:
        with get_db() as db:
            for camera in cameras:
                db_camera = CameraModel(id=camera.id, user_id=user.id)
                db.add(db_camera)
                db.commit()
                db.refresh(db_camera)

    def get(self, user_id: int) -> List[CameraModel]:
        with get_db() as db:
            return db.query(CameraModel).filter(CameraModel.user_id == user_id).all()
