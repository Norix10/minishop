from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    abstract = True
    id: Mapped[int] = mapped_column(primary_key=True)
