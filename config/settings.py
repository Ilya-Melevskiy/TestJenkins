import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "")
    timeout: int = int(os.getenv("API_TIMEOUT", "10"))


settings = Settings()
