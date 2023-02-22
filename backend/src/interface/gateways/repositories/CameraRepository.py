from src.domain.models.CameraModel import CameraModel


class CameraRepository:
    def add(self, camera: CameraModel) -> None:
        raise NotImplementedError
