from fastapi import APIRouter
from pydantic import BaseModel

from src.application.usecases.user_usecase import UserUsecase

router = APIRouter()


class Camera(BaseModel):
    id: int


class UserRequest(BaseModel):
    name: str
    cameras: list[Camera]


userUsecase = UserUsecase()


@router.post("/user")
def add_user(user_request: UserRequest):
    userUsecase.register()
    results = {"message": "user and cameras are registered."}
    return results
