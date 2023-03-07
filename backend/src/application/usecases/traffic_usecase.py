from src.interface.gateways.repositories.CameraRepository import CameraRepository
from src.interface.gateways.repositories.UserRepository import UserRepository
from src.interface.gateways.external_apis.camera_external_api import CameraExternalApi


class TrafficUsecase:
    def __init__(self):
        self.user_repository = UserRepository()
        self.camera_repository = CameraRepository()
        self.camera_external_api = CameraExternalApi()

    def get_traffic(self, user_id: int):
        user = self.user_repository.get(user_id)
        cameras = self.camera_repository.get(user_id)
        cameras_with_count = self.camera_external_api.get(cameras)
        return user, cameras_with_count
