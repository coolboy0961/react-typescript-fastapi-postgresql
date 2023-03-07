from src.interface.gateways.repositories.models.use_model import UserModel
from src.infrastructure.database import get_db
from src.domain.entities.user_entity import UserEntity


class UserRepository:
    def add(self, user: UserEntity) -> None:
        with get_db() as db:
            db_user = UserModel(id=user.id, name=user.name)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

    def get(self, user_id: int) -> UserModel:
        with get_db() as db:
            return db.query(UserModel).filter(UserModel.id == user_id).first()
