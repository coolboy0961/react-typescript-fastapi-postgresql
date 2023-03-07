from src.exception.custom_exception import CustomException


class ErrorCodes:
    @classmethod
    def SP422001(cls):
        return CustomException(422, "SP422001", "APIリクエストのパラメータチェックが失敗しました。")

    @classmethod
    def SP400002(cls):
        return CustomException(400, "SP400002", "ユーザが利用しようとしているカメラは存在しません。")