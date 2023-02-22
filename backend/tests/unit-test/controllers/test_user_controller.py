import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from src.application.usecases.user_usecase import UserUsecase


@pytest.mark.skip(reason="最初に書くテストケースです。usecaseを呼び出す前に書いたテストケースなので、usecaseを呼び出すと失敗してしまう")
def test_ユーザと利用するカメラを登録するAPIをコールして正常時のResponseを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected = {"message": "user and cameras are registered."}

    # Act
    response = client.post("/user", headers={"Content-Type": "application/json"}, json={
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
    response = client.post("/user", headers={"Content-Type": "application/json"}, json={
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
    expected = {"message": "user and cameras are registered."}
    user_usecase_mock = mocker.patch.object(UserUsecase, "register")

    # Act
    response = client.post("/user", headers={"Content-Type": "application/json"}, json={
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
    user_usecase_mock.assert_called_once()


def test_nameパラメータが空の場合正しいエラーレスポンスを返すこと(client: TestClient, mocker: MockFixture):
    # Arrange
    expected_status_code = 400
    expected_response = {
        "error_code": "SP400001",
        "message": "name should not be empty."
    }
    user_usecase_mock = mocker.patch.object(UserUsecase, "register")

    # Act
    response = client.post("/user", headers={"Content-Type": "application/json"}, json={
        "name": "",
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
