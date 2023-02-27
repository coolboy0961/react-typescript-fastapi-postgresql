


from src.interface.gateways.repositories.models.CameraModel import CameraModel


class CameraRepository:
    def add(self, camera: CameraModel) -> None:
        raise NotImplementedError
