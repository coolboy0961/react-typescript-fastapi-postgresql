from typing import List
from src.domain.entities.CameraEntity import CameraEntity
from src.domain.entities.UserEntity import UserEntity
from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository


class UserUsecase:
    def register(self, user: UserEntity, cameras: List[CameraEntity]) -> None:
        UserRepository().add(user)
        CameraRepository.add(cameras)
