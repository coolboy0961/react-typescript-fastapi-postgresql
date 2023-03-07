from pytest_mock import MockFixture
from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity
from src.interface.gateways.repositories.camera_repository import CameraRepository
from src.interface.gateways.repositories.user_repository import UserRepository
from src.interface.gateways.external_apis.camera_external_api import CameraExternalApi
from src.application.usecases.traffic_usecase import TrafficUsecase


def test_TrafficUsecaseからリポジトリを使ってユーザとカメラ情報を取得できること(mocker: MockFixture):
    # Arrange
    expected_user = UserEntity("1", "Tom")
    expected_cameras = [
        CameraEntity(1, 35),
        CameraEntity(2, 67),
        CameraEntity(3, 19),
    ]
    user_repository_mock = mocker.patch.object(
        UserRepository, "get", return_value=UserEntity("1", "Tom"))
    camera_repository_mock = mocker.patch.object(CameraRepository, "get", return_value=[
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0),
    ])
    camera_external_api_mock = mocker.patch.object(CameraExternalApi, "get", return_value=[
        CameraEntity(1, 35),
        CameraEntity(2, 67),
        CameraEntity(3, 19),
    ])

    # Act
    target = TrafficUsecase()
    actual_user, actual_cameras = target.get_traffic(1)

    # Assert
    assert actual_user == expected_user
    assert actual_cameras == expected_cameras
    user_repository_mock.assert_called_once_with(1)
    camera_repository_mock.assert_called_once_with(1)
    camera_external_api_mock.assert_called_once_with([
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0),
    ])
