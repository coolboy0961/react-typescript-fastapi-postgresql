from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Camera(BaseModel):
    id: int


class UserRequest(BaseModel):
    name: str
    cameras: list[Camera]


@router.post("/user")
def add_user(user_request: UserRequest):
    results = {"message": "user and cameras are registered."}
    return results
