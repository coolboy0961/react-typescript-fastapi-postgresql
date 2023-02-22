from src.exception.CustomException import CustomException


class ErrorCodes:
    @classmethod
    def SP422001(cls):
        return CustomException(422, "SP422001", "APIリクエストのパラメータチェックが失敗しました.")
