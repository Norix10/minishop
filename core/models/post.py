from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .user import User

class Post(Base):
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user:Mapped["User"] = relationship(back_populates="posts")