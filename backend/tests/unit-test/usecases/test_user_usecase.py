import pytest
from pytest_mock import MockFixture
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity

from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository
from src.interface.gateways.external_apis.CameraExternalApi import CameraExternalApi

from src.application.usecases.UserUsecase import UserUsecase
from src.exception.ErrorCodes import ErrorCodes


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


# def test_ユーザと利用するカメラを登録するusecaseをコールして外部システムのAPIをコールしてnot_foundエラーが返ってきた場合正しいエラーをthrowする():
#     # Arrange
#     excepted_exception = ErrorCodes.SP400002()
#     excepted_exception.detail = {
#         "user_id": 1,
#         "not_found_cameras": [2, 3]
#     }

#     # Act
#     user_repository_mock = mocker.patch.object(UserRepository, "add")
#     camera_repository_mock = mocker.patch.object(CameraRepository, "add")

#     # Assert
