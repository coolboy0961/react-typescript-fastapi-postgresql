import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from sqlalchemy.orm import Session
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.models.UserModel import UserModel
from src.interface.gateways.repositories.UserRepository import UserRepository


# @pytest.mark.skip("未完成")

def test_ユーザを登録するリポジトリをコールしてユーザ情報が登録されること(unit_test_db: Session, mocker: MockFixture):
    # Arrange
    excepted_user_model = UserModel(id=1, name="Tom")

    # Act
    target = UserRepository()
    user_entity = UserEntity(
        excepted_user_model.id, excepted_user_model.name)
    target.add(user_entity, unit_test_db)

    actual_user_modal = unit_test_db.query(UserModel).first()

    print(jsonable_encoder(actual_user_modal))

    # Assert
    assert jsonable_encoder(
        excepted_user_model) == jsonable_encoder(actual_user_modal)
