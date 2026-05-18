from sqlalchemy import create_engine, text

from tennis_scoreboard.config import SETTINGS

engine = create_engine(url=SETTINGS.database_url_pymysql, echo=True)

with engine.connect() as conn:
    result = conn.execute(text('SELECT VERSION()'))
    print(f'{result.first()=}')
