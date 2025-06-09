from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Song(Base):
    __tablename__ = "songs"

    name: Mapped[str] = mapped_column(primary_key=True, index=True)
    artist: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    year_released: Mapped[int] = mapped_column(nullable=False)
    album: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"{self.name!r} ({self.artist!r})"
