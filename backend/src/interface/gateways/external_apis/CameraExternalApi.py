from src.infrastructure.ExternalApiClient import ExternalApiClient
from src.domain.entities.CameraEntity import CameraEntity


class CameraExternalApi:
    def get(self, cameras: list[CameraEntity]):
        request_ids = []
        for camera in cameras:
            request_ids.append(str(camera.id))
        request_ids_str = ",".join(request_ids)
        response = ExternalApiClient().get(f"/camera?ids={request_ids_str}")
        data = response.json()
        for camera in cameras:
            camera.count = self.find_count_from_cameras_json_array(data, camera.id)
        return cameras

    def find_count_from_cameras_json_array(self, json_array: list[dict], id: int):
        for keyval in json_array:
            if id == keyval['id']:
                return keyval["count"]
