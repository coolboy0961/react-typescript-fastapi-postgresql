from fastapi import APIRouter

from src.application.usecases.traffic_usecase import TrafficUsecase

router = APIRouter(prefix="/api")

# traffic情報はuser_idによって取得され、usersと関連があるため、パスを"/v1/users/{user_id}/traffic"の形にした
@router.get("/v1/users/{user_id}/traffic")
def get_traffic(user_id: int):
    # get_trafficメソッドの戻り値はuserとcamerasのタプルであるため、userとcamerasにそれぞれ代入している
    user, cameras = TrafficUsecase().get_traffic(user_id)
    return {
        "name": user.name,
        # この部分はリスト内包表記で書かれており、camerasの中身を一つずつ辞書に変換してリストにしている
        "cameras": [{"id": camera.id, "count": camera.count} for camera in cameras],
    }
