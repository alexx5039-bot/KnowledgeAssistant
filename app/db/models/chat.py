from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base import BaseModel
from app.db.models.user import User

class Chat(BaseModel):
    __tablename__ = "chats"

    question = Mapped[str] = mapped_column(Text)
    answer = Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["User"] = relationship(
        back_populates="chats",
        lazy="selectin"
    )