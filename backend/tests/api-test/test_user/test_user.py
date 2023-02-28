
import pytest
import requests
from fastapi.encoders import jsonable_encoder
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.UserModel import UserModel
from src.interface.gateways.repositories.models.CameraModel import CameraModel

@pytest.mark.parametrize("json_server", ["tests/api-test/test_user/external_api_response/camera_ok.json"], indirect=True)
def test_ユーザと利用するカメラを登録するAPIをコールして正常時のResponseを返すこと(json_server, reset_db):
    # Arrange
    expected = {"message": "user and cameras are registered."}
    excepted_user_model = UserModel(id=1, name="Tom")
    expected_camera_models = [
        CameraModel(id=1, user_id=1),
        CameraModel(id=2, user_id=1),
        CameraModel(id=3, user_id=1)
    ]

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
    with get_db() as db:
        actual_user_modal = db.query(UserModel).first()
        actual_camera_modal = db.query(CameraModel).all()

    # Assert
    assert response.status_code == 200
    assert actual == expected
    assert jsonable_encoder(
        excepted_user_model) == jsonable_encoder(actual_user_modal)
    assert jsonable_encoder(
        expected_camera_models) == jsonable_encoder(actual_camera_modal)