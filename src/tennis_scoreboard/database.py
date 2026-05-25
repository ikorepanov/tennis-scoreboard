from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from tennis_scoreboard.config import SETTINGS

engine = create_engine(url=SETTINGS.database_url_pymysql, echo=True)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
