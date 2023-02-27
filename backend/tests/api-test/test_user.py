import requests


def test_ユーザと利用するカメラを登録するAPIをコールして正常時のResponseを返すこと(reset_db):
    # Arrange
    expected = {"message": "user and cameras are registered."}

    # Act
    response = requests.post("http://localhost:8000/user", headers={"Content-Type": "application/json"}, json={
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
    assert actual == expected
