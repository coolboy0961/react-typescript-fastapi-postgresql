from src.infrastructure.external_api_client import ExternalApiClient

def test_ExternalApiClientのgetメソッドで情報を取得することができること(requests_mock):
    # Arrange
    expected = {
        "id": 1,
        "message": "this is a get test."
    }

    requests_mock.get("http://localhost:1234/api/get-test", json={
        "id": 1,
        "message": "this is a get test."
    })
    
    # Act
    target = ExternalApiClient()
    actual = target.get("/get-test").json()
    
    # Assert
    assert expected == actual
