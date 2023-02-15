from fastapi.testclient import TestClient


def test_ユーザと利用するカメラを登録するAPIをコールできること(client: TestClient):
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
