from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_ROOT_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def DATABASE_URL_pymysql(self):
        return URL.create(
            drivername='mysql+pymysql',
            username=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.MYSQL_DATABASE,
        )

    model_config = SettingsConfigDict(env_file='.env')


SETTINGS = Settings()  # type: ignore[reportCallIssue]
