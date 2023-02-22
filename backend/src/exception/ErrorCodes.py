from src.exception.CustomException import CustomException


class ErrorCodes:
    @classmethod
    def SP400001(cls):
        return CustomException(400, "SP400001", "name should not be empty.")
