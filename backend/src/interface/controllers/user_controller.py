from fastapi import APIRouter
from pydantic import BaseModel

from src.domain.entities.camera_entity import CameraEntity
from src.domain.entities.user_entity import UserEntity
from src.exception.error_codes import ErrorCodes
from src.application.usecases.user_usecase import UserUsecase

router = APIRouter(prefix="/api")


class Camera(BaseModel):
    id: int


class UserRequest(BaseModel):
    id: int
    name: str
    cameras: list[Camera]


userUsecase = UserUsecase()


@router.post("/v1/users")
def add_user(user_request: UserRequest):
    userUsecase.register(
        convert_user_request_to_user_entity(user_request),
        convert_cameras_request_to_camera_entitys(user_request.cameras)
    )
    results = {"message": "user and cameras are registered."}
    return results


def convert_user_request_to_user_entity(request: UserRequest):
    return UserEntity(request.id, request.name)


def convert_cameras_request_to_camera_entitys(request: list[Camera]):
    camera_entiies = []
    for camera_request in request:
        camera_entiies.append(CameraEntity(camera_request.id, 0))
    return camera_entiies

