from fastapi.testclient import TestClient


def test_交通量検索APIを呼び出して正常時のResponseを取得できること(client: TestClient):

    # Arrange
    expected = {
        "name": "Tom",
        "camera": [
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

    # Act
    response = client.get("/api/v1/users/1/traffic")
    actual= response.json()

    # Assert
    assert response.status_code == 200
    assert actual == expected
