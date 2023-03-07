import pytest
from pytest_mock import MockFixture
from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity

from src.interface.gateways.repositories.camera_repository import CameraRepository
from src.interface.gateways.repositories.user_repository import UserRepository
from src.interface.gateways.external_apis.camera_external_api import CameraExternalApi

from src.application.usecases.user_usecase import UserUsecase
from src.exception.error_codes import ErrorCodes


def test_ユーザと利用するカメラを登録するusecaseをコールして登録用リポジトリが呼び出されること(mocker: MockFixture):
    # Arrange
    excepted_user = UserEntity(1, "Tom")
    excepted_cameras = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    user_repository_mock = mocker.patch.object(UserRepository, "add")
    camera_repository_mock = mocker.patch.object(CameraRepository, "add")
    mocker.patch.object(CameraExternalApi, "get")

    # Act
    target = UserUsecase()

    target.register(excepted_user, excepted_cameras)

    # Assert
    user_repository_mock.assert_called_once_with(excepted_user)
    camera_repository_mock.assert_called_once_with(
        excepted_cameras, excepted_user)


def test_ユーザと利用するカメラを登録するusecaseをコールして外部システムのAPIをコールすること(mocker: MockFixture):
    # Arrange
    excepted_cameras = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    mocker.patch.object(UserRepository, "add")
    mocker.patch.object(CameraRepository, "add")
    camera_external_api = mocker.patch.object(CameraExternalApi, "get")

    # Act
    target = UserUsecase()
    input_user = UserEntity(1, "Tom")
    target.register(input_user, excepted_cameras)

    # Assert
    camera_external_api.assert_called_once_with(excepted_cameras)
