from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from backend.src.application.usecases.user_usecase import UserUsecase


def test_ユーザと利用するカメラを登録するAPIをコールして登録用のusecaseを呼び出して正常時のResponseを返すこと(client: TestClient, mocker: MockFixture):
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