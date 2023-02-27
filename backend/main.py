from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
from src.exception.ErrorCodes import ErrorCodes
from src.exception.CustomException import CustomException

from src.interface.controllers import items_controller
from src.interface.controllers import user_controller

from src.infrastructure.database import Base, engine

logger = logging.getLogger('uvicorn')

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Exception):
    logger.error("予期せぬエラーが発生しました。" + str(exception))
    return JSONResponse(
        status_code=500,
        content={
            "message": f"予期せぬエラーが発生しました。"
        },
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, request_validation_exception: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error_code": ErrorCodes.SP422001().error_code,
            "message": ErrorCodes.SP422001().message,
            "detail": request_validation_exception.errors()
        }
    )


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, custom_exception: CustomException):
    logger.error("エラーが発生しました。" + str(custom_exception))
    logger.error("リクエスト：" + str(request))
    return JSONResponse(
        status_code=custom_exception.status_code,
        content={
            "error_code": custom_exception.error_code,
            "message": custom_exception.message
        },
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(items_controller.router)
app.include_router(user_controller.router)
