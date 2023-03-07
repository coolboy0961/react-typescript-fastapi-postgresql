from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.database import Base


class CameraModel(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.user_id == other.user_id)
