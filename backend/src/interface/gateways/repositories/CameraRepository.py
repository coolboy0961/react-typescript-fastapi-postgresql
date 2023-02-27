from src.domain.entities.CameraEntity import CameraEntity
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.CameraModel import CameraModel
from src.domain.entities.UserEntity import UserEntity


class CameraRepository:
    def add(self, cameras: CameraEntity, user: UserEntity) -> None:
        with get_db() as db:
            for camera in cameras:
                db_camera = CameraModel(id=camera.id, user_id=user.id)
                db.add(db_camera)
                db.commit()
                db.refresh(db_camera)