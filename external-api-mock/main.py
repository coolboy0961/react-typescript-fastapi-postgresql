from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/camera")
def camera_mock():
    return [
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
        }
    ]
