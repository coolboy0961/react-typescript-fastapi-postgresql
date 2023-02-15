from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    # return {"item_id": item_id, "name": name} # エラーハンドラーの動作確認をするため
    return {"item_id": item_id}