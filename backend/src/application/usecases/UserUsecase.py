from typing import List
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository
from src.interface.gateways.external_apis.CameraExternalApi import CameraExternalApi


class UserUsecase:
    def register(self, user: UserEntity, cameras: List[CameraEntity]) -> None:
        CameraExternalApi().get(cameras)
        UserRepository().add(user)
        CameraRepository().add(cameras, user)
