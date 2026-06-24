from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.user import User
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    filename: Mapped[str] = mapped_column(String(255))
    chunks_count: Mapped[int]
    file_path: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["User"] = relationship(
        back_populates="documents"
    )
