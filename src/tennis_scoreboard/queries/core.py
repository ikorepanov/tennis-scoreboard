from tennis_scoreboard.database import engine, session_factory
from tennis_scoreboard.models import Player, metadata_obj


def create_tables() -> None:
    engine.echo = False
    metadata_obj.drop_all(engine)  # удалить все таблицы
    metadata_obj.create_all(engine)
    engine.echo = True


def insert_data() -> None:
    with session_factory() as session:
        player = Player(name='Some')
        session.add_all([player])
        session.commit()
