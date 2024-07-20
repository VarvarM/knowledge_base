from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class SettingsTest(BaseSettings):
    ADDON_HOST: str
    ADDON_PORT: int
    ADDON_USER: str
    ADDON_PASSWORD: str
    ADDON_DB: str
    ADDON_URI: str

    @property
    def DATABASE_URL(self):
        return f'postgresql+psycopg{self.ADDON_URI}'

    class ConfigTest:
        env_file = '.env'


settings = SettingsTest()

# print(settings.model_dump())
