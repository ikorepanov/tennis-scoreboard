from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column

from tennis_scoreboard.database import Base

metadata_obj = MetaData()


# Предусмотреть - Индекс колонки Name, для эффективности поиска игроков по имени
class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Match(Base):
    __tablename__ = 'matches'
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[str]
    player_1: Mapped[int]
    player_2: Mapped[int]
    winner: Mapped[int]
    score: Mapped[str]
