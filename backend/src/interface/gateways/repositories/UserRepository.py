from src.domain.models.UserModel import UserModel


class UserRepository:
    def add(self, user: UserModel) -> None:
        raise NotImplementedError
