from src.interface.gateways.repositories.models.UserModel import UserModel
from src.infrastructure.database import get_db
from src.domain.entities.UserEntity import UserEntity


class UserRepository:
    def add(self, user: UserEntity) -> None:
        with get_db() as db:
            db_user = UserModel(id=user.id, name=user.name)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
    def get(self, user_id: int):
        raise NotImplementedError("This method is not yet implemented.")
