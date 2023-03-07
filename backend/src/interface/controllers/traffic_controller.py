from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/v1/users/{user_id}/traffic")
def get_traffic(user_id: int):
    traffic_data = {
        "name": "Tom",
        "camera": [
                {
                    "id": 1,
                    "count": 35
                },
            {
                    "id": 2,
                    "count": 67
                },
            {
                    "id": 3,
                    "count": 19
                },
        ]
    }
    return traffic_data