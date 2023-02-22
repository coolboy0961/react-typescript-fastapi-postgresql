from typing import List
from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository
from src.domain.models.CameraModel import CameraModel
from src.domain.models.UserModel import UserModel


class UserUsecase:
    def register(self, user: UserModel, cameras: List[CameraModel]) -> None:
        UserRepository().add(user)
        CameraRepository.add(cameras)
