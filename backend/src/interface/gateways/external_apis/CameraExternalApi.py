from src.domain.entities.CameraEntity import CameraEntity

class CameraExternalApi:
    def get(self, cameras: list[CameraEntity]):
        raise NotImplementedError()