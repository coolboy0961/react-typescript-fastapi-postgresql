from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity
from src.application.usecases.traffic_usecase import TrafficUsecase


def test_交通量検索APIを呼び出して正常時のResponseを取得できること(client: TestClient, mocker: MockFixture):

    # Arrange
    expected = {
        "name": "Tom",
        "cameras": [
            {
                "id": 1,
                "count": 35
            },
            {
                "id": 2,
                "count": 67
            },
            {
                "id": 3,
                "count": 19
            },
        ]
    }
    user = UserEntity(1, "Tom")
    cameras = [
        CameraEntity(1, 35),
        CameraEntity(2, 67),
        CameraEntity(3, 19),
    ]
    traffic_usercase_mock = mocker.patch.object(
        TrafficUsecase, "get_traffic", return_value=[user, cameras])

    # Act
    response = client.get("/api/v1/users/1/traffic")
    actual = response.json()

    # Assert
    assert response.status_code == 200
    assert actual == expected
    traffic_usercase_mock.assert_called_once_with(1)


def test_交通量検索APIを呼び出してuser_idがintではない場合正しいエラーレスポンスを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected = {
        "error_code": "SP422001",
        "message": "APIリクエストのパラメータチェックが失敗しました。",
        "detail": [{"loc": ["path", "user_id"], "msg": "value is not a valid integer", "type": "type_error.integer"}]
    }
    user = UserEntity(1, "Tom")
    cameras = [
        CameraEntity(1, 35),
        CameraEntity(2, 67),
        CameraEntity(3, 19),
    ]
    traffic_usercase_mock = mocker.patch.object(
        TrafficUsecase, "get_traffic", return_value=[user, cameras])

    # Act
    response = client.get("/api/v1/users/abc/traffic")
    actual = response.json()

    # Assert
    assert response.status_code == 422
    assert actual == expected
    traffic_usercase_mock.assert_not_called()
