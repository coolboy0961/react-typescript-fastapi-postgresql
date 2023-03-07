from typing import List
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository
from src.interface.gateways.external_apis.camera_external_api import CameraExternalApi


class UserUsecase:
    def __init__(self) -> None:
        self.camera_external_api = CameraExternalApi()
        self.user_repository = UserRepository()
        self.camera_repository = CameraRepository()

    def register(self, user: UserEntity, cameras: List[CameraEntity]) -> None:
        self.camera_external_api.get(cameras)
        self.user_repository.add(user)
        self.camera_repository.add(cameras, user)
