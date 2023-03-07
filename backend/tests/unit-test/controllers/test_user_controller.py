import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from src.exception.error_codes import ErrorCodes

from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity

from src.application.usecases.user_usecase import UserUsecase


@pytest.mark.skip(reason="最初に書くテストケースです。usecaseを呼び出す前に書いたテストケースなので、usecaseを呼び出すと失敗してしまう")
def test_ユーザと利用するカメラを登録するAPIをコールして正常時のResponseを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected = {"message": "user and cameras are registered."}

    # Act
    response = client.post("/api/v1/api/v1/userss", headers={"Content-Type": "application/json"}, json={
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })
    actual = response.json()

    # Assert
    assert response.status_code == 200
    assert actual == expected


@pytest.mark.skip(reason="2番目に書くテストケースです。usecaseを呼び出す実装をうながすためのテストケース")
def test_ユーザと利用するカメラを登録するAPIをコールして登録用のusecaseを呼び出すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    # UserUsecaseクラスのメンバーメソッドをモック
    user_usecase_mock = mocker.patch.object(UserUsecase, "register")

    # Act
    response = client.post("/api/v1/users", headers={"Content-Type": "application/json"}, json={
        "id": 1,
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })

    # Assert
    assert response.status_code == 200
    user_usecase_mock.assert_called_once()


def test_ユーザと利用するカメラを登録するAPIをコールして登録用のusecaseを呼び出して正常時のResponseを返すこと(client: TestClient, mocker: MockFixture):
    """
    2番目のテストケースを書き終わった後、リファクタリング段階で、1番目と2番目のテストケースを一つにすることができることがわかり、
    3番目のテストケースとして作成した
    """
    # Arrange
    expected_response = {"message": "user and cameras are registered."}
    expected_input_user = UserEntity(1, "Tom")
    expected_input_cameras = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0),
    ]
    user_usecase_mock = mocker.patch.object(UserUsecase, "register")

    # Act
    response = client.post("/api/v1/users", headers={"Content-Type": "application/json"}, json={
        "id": 1,
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })
    actual = response.json()

    # Assert
    assert response.status_code == 200
    assert actual == expected_response
    user_usecase_mock.assert_called_once_with(
        expected_input_user, expected_input_cameras)


def test_idパラメータが空の場合正しいエラーレスポンスを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected_status_code = 422
    expected_response = {
        "error_code": "SP422001",
        "message": "APIリクエストのパラメータチェックが失敗しました。",
        "detail": [{
            "loc": ["body", "id"],
            "msg": "field required",
            "type": "value_error.missing"}]
    }
    user_usecase_mock = mocker.patch.object(UserUsecase, "register")

    # Act
    response = client.post("/api/v1/users", headers={"Content-Type": "application/json"}, json={
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })
    actual_status_code = response.status_code
    acture_response = response.json()

    # Assert
    assert expected_status_code == actual_status_code
    assert expected_response == acture_response
    user_usecase_mock.assert_not_called()


def test_ユーザと利用するカメラを登録するAPIをコールして登録しようとするcameraが存在しない時に正しいエラーレスポンスを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected_status_code = 400
    expected_error_response = {
        "error_code": "SP400002",
        "message": "ユーザが利用しようとしているカメラは存在しません。",
        "detail": {
            "not_found_cameras": [2, 3]
        }
    }
    error = ErrorCodes.SP400002()
    error.detail = {
        "not_found_cameras": [2, 3]
    }
    user_usecase_mock = mocker.patch.object(
        UserUsecase, "register", side_effect=error)

    # Act
    response = client.post("/api/v1/users", headers={"Content-Type": "application/json"}, json={
        "id": 1,
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })
    actual_status_code = response.status_code
    acture_response = response.json()

    # Assert
    assert expected_status_code == actual_status_code
    assert expected_error_response == acture_response
    user_usecase_mock.assert_called()
