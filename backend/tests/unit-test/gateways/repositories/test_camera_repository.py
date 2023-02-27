import pytest
from sqlalchemy.orm import Session
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.models.CameraModel import CameraModel
from fastapi.encoders import jsonable_encoder


def test_カメラを登録するリポジトリをコールしてカメラ情報が登録されること(unit_test_db: Session):
    # Arrange
    expected_camera_model = CameraModel(id=1, user_id=1)

    # Act
    target = CameraRepository()
    camera_entity = CameraEntity(1, 0)
    user_entity = UserEntity(1, "Tom")
    target.add(camera_entity, user_entity, unit_test_db)

    actual_camera_modal = unit_test_db.query(CameraModel).first()

    # Assert
    assert jsonable_encoder(
        expected_camera_model) == jsonable_encoder(actual_camera_modal)
