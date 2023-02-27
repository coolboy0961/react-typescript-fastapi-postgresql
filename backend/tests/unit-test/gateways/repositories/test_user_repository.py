import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.models.UserModel import UserModel
from src.interface.gateways.repositories.UserRepository import UserRepository



# @pytest.mark.skip("未完成")


def test_ユーザを登録するリポジトリをコールしてユーザ情報が登録されること(unit_test_db, mocker: MockFixture):
    # Arrange
    excepted_user = UserEntity(1, "Tom")

    # Act
    target = UserRepository()
    # target.add(excepted_user)
    db_user = UserModel(id=1, name="Tom")
    unit_test_db.add(db_user)
    unit_test_db.commit()
    unit_test_db.refresh(db_user)

    actual_user = unit_test_db.query(UserModel)

    # Assert
    assert excepted_user == actual_user
