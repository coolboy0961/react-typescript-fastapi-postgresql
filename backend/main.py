from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from src.interface.controllers import items_controller

logger = logging.getLogger('uvicorn')

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(items_controller.router)
