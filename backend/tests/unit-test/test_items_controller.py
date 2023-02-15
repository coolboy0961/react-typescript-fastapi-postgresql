from fastapi.testclient import TestClient


def test_read_main(client):
    # Arrange
    expected = {"item_id": "1,2,3"}

    # Act
    response = client.get("/items/1,2,3")
    actual = response.json()

    # Assert
    assert response.status_code == 200
    assert actual == expected
