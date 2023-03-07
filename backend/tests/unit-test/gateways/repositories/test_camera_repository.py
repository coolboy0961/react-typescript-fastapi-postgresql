import pytest
from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity
from src.interface.gateways.repositories.camera_repository import CameraRepository
from src.interface.gateways.repositories.models.camera_model import CameraModel
from src.interface.gateways.repositories.models.use_model import UserModel
from fastapi.encoders import jsonable_encoder
from src.infrastructure.database import get_db


def test_カメラを登録するリポジトリをコールしてカメラ情報が登録されること(reset_db):
    # Arrange
    expected_camera_models = [
        CameraModel(id=1, user_id=1),
        CameraModel(id=2, user_id=1),
        CameraModel(id=3, user_id=1)
    ]

    # Act
    target = CameraRepository()
    camera_entitys = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    user_entity = UserEntity(1, "Tom")
    target.add(camera_entitys, user_entity)

    with get_db() as db:
        actual_camera_modal = db.query(CameraModel).all()

    # Assert
    assert jsonable_encoder(
        expected_camera_models) == jsonable_encoder(actual_camera_modal)


def test_登録されているカメラ情報をuser_idで取得できること(reset_db):
    # Arrange
    expected_camera_models = [
        CameraModel(id=1, user_id=1),
        CameraModel(id=2, user_id=1),
        CameraModel(id=3, user_id=1)
    ]

    camera_entitys = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    user_entity = UserEntity(1, "Tom")
    CameraRepository().add(camera_entitys, user_entity)

    # Act
    target = CameraRepository()
    actual_camera_models = target.get(1)

    # Assert
    assert actual_camera_models == expected_camera_models
