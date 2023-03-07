from src.exception.custom_exception import CustomException
from src.exception.error_codes import ErrorCodes
from src.interface.gateways.external_apis.camera_external_api import CameraExternalApi
from src.domain.entities.camera_entity import CameraEntity
from fastapi.encoders import jsonable_encoder


def test_CameraExternalApiのgetメソッドでカメラの検知回数を取得できること(requests_mock):
    # Arrange
    expected = [
        CameraEntity(1, 35),
        CameraEntity(2, 67),
        CameraEntity(3, 19)
    ]
    requests_mock.get('http://localhost:1234/api/v1/camera?ids=1,2,3', json=[
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
    ])

    # Act
    target = CameraExternalApi()
    input_cameras = [
        CameraEntity(1, 0),
        CameraEntity(2, 0),
        CameraEntity(3, 0)
    ]
    actual = target.get(input_cameras)

    # Assert
    assert requests_mock.call_count == 1
    assert expected == actual


def test_id指定でJSON配列から要素を取得できること():
    # Arrange
    excepted = 67

    # Act
    target = CameraExternalApi()
    input_json_array = [
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
    actual = target.find_count_from_cameras_json_array(input_json_array, 2)

    # Assert
    assert excepted == actual


def test_外部APIからcamera_not_foundのエラーが返ってくる場合正しいエラーをthrowすること(requests_mock):
    # Arrange
    excepted_exception = ErrorCodes.SP400002()
    excepted_exception.detail = {
        "not_found_cameras": [2, 3]
    }
    requests_mock.get(
        'http://localhost:1234/api/v1/camera?ids=1,2,3',
        status_code=404,
        json={
            "error_code": "CR000001",
            "message": "following ids is not found. ",
            "details": {
                "ids": [2, 3]
            }
        }
    )

    # Act
    try:
        target = CameraExternalApi()
        input_cameras = [
            CameraEntity(1, 0),
            CameraEntity(2, 0),
            CameraEntity(3, 0)
        ]
        target.get(input_cameras)
    except CustomException as e:
        actual_exception = e

    # Assert
    assert jsonable_encoder(
        excepted_exception) == jsonable_encoder(actual_exception)
