from pydantic_settings  import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str
    CODECOV_TOKEN: str
    GITHUB_ACCESS_TOKEN: str

settings = Settings()
