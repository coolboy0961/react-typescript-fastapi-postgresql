from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.exception.ErrorCodes import ErrorCodes

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
    if user_request.name == "":
        raise ErrorCodes.SP400001()

    userUsecase.register()
    results = {"message": "user and cameras are registered."}
    return results
