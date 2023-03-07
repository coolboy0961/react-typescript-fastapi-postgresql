from fastapi import APIRouter

from src.application.usecases.TrafficUsecase import TrafficUsecase

router = APIRouter(prefix="/api")

# traffic情報はuser_idによって取得され、usersと関連があるため、パスを"/v1/users/{user_id}/traffic"の形にした
@router.get("/v1/users/{user_id}/traffic")
def get_traffic(user_id: int):
    user, cameras = TrafficUsecase().get_traffic(user_id)
    return {
        "name": user.name,
        "cameras": [{"id": camera.id, "count": camera.count} for camera in cameras],
    }
