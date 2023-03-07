import pytest
from fastapi.encoders import jsonable_encoder
from pytest_mock import MockFixture
from src.domain.entities.user_entity import UserEntity
from src.interface.gateways.repositories.models.use_model import UserModel
from src.interface.gateways.repositories.user_repository import UserRepository
from src.infrastructure.database import get_db


def test_ユーザを登録するリポジトリをコールしてユーザ情報が登録されること(reset_db, mocker: MockFixture):
    # Arrange
    excepted_user_model = UserModel(id=1, name="Tom")

    # Act
    target = UserRepository()
    user_entity = UserEntity(
        excepted_user_model.id, excepted_user_model.name)
    target.add(user_entity)

    with get_db() as db:
        actual_user_modal = db.query(UserModel).first()

    print(jsonable_encoder(actual_user_modal))

    # Assert
    assert jsonable_encoder(
        excepted_user_model) == jsonable_encoder(actual_user_modal)
