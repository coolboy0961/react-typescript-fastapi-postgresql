import json
import requests
from wiremock.client import Mappings, Mapping, MappingRequest, MappingResponse
from src.infrastructure.database import get_db
from src.interface.gateways.repositories.models.use_model import UserModel
from src.interface.gateways.repositories.models.camera_model import CameraModel


def test_交通量検索APIを呼び出して正常時のReponseを取得できること(reset_db, wiremock_server):
    # Arrange
    expected_response = {
        "name": "Tom",
        "cameras": [
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

    with get_db() as db:
        db_user = UserModel(id=1, name="Tom")
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        camera_models = [
            CameraModel(id=1, user_id=1),
            CameraModel(id=2, user_id=1),
            CameraModel(id=3, user_id=1)
        ]
        for db_camera in camera_models:
            db.add(db_camera)
            db.commit()
            db.refresh(db_camera)

    # Act
    response = requests.get("http://localhost:8000/api/v1/users/1/traffic")
    actual_response = response.json()

    # Assert
    assert actual_response == expected_response
