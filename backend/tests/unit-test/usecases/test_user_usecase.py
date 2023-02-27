import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity

from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository

from src.application.usecases.user_usecase import UserUsecase


def test_ユーザと利用するカメラを登録するusecaseをコールして登録用リポジトリが呼び出されること(client: TestClient, mocker: MockFixture):
    # Arrange
    excepted_user = UserEntity(1, "Tom")
    excepted_cameras = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    user_repository_mock = mocker.patch.object(UserRepository, "add")
    camera_repository_mock = mocker.patch.object(CameraRepository, "add")

    # Act
    target = UserUsecase()

    target.register(excepted_user, excepted_cameras)

    # Assert
    user_repository_mock.assert_called_once_with(excepted_user)
    camera_repository_mock.assert_called_once_with(excepted_cameras)
