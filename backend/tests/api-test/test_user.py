
import json
import requests
from fastapi.encoders import jsonable_encoder
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.use_model import UserModel
from src.interface.gateways.repositories.models.camera_model import CameraModel
from wiremock.client import Mappings, Mapping, MappingRequest, MappingResponse


def test_ユーザと利用するカメラを登録するAPIをコールして正常時のResponseを返すこと(reset_db, wiremock_server):
    # Arrange
    expected = {"message": "user and cameras are registered."}
    excepted_user_model = UserModel(id=1, name="Tom")
    expected_camera_models = [
        CameraModel(id=1, user_id=1),
        CameraModel(id=2, user_id=1),
        CameraModel(id=3, user_id=1)
    ]
    mock_camera_api = Mapping(
        request=MappingRequest(
            method="GET",
            url="/api/v1/camera?ids=1,2,3"  # http://localhost:3000/api/v1/camera?ids=1,2,3
        ),
        response=MappingResponse(
            status=200,
            body=json.dumps([
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
                }
            ])
        ),
    )
    Mappings.create_mapping(mapping=mock_camera_api)

    # Act
    response = requests.post("http://localhost:8000/api/v1/users", headers={"Content-Type": "application/json"}, json={
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


def test_ユーザと利用するカメラを登録するAPIをコールして存在しないカメラがある時に正しいエラーレスポンスを返すこと(reset_db, wiremock_server):
    # Arrange
    expected_status_code = 400
    expected_error_response = {
        "error_code": "SP400002",
        "message": "ユーザが利用しようとしているカメラは存在しません。",
        "detail": {
            "not_found_cameras": [2, 3]
        }
    }
    mock_camera_api = Mapping(
        request=MappingRequest(
            method="GET",
            url="/api/v1/camera?ids=1,2,3"
        ),
        response=MappingResponse(
            status=404,
            body=json.dumps({
                "error_code": "CR000001",
                "message": "following ids is not found. ",
                "details": {
                    "ids": [2, 3]
                }
            })
        ),
    )
    Mappings.create_mapping(mapping=mock_camera_api)

    # Act
    response = requests.post("http://localhost:8000/api/v1/users", headers={"Content-Type": "application/json"}, json={
        "id": 1,
        "name": "Tom",
        "cameras": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    })
    actual_response = response.json()
    actual_status_code = response.status_code
    with get_db() as db:
        actual_user_modal = db.query(UserModel).all()
        actual_camera_modal = db.query(CameraModel).all()

    # Assert
    assert actual_status_code == expected_status_code
    assert actual_response == expected_error_response
    assert len(actual_user_modal) == 0
    assert len(actual_camera_modal) == 0
