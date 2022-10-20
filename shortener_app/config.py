from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"
    class Config:
        env_file=".env"


# @lru_cache decorator allows you to cache the 
# result of get_settings() using the LRU strategy
# least recently used
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
# @lru_cache decorator, you made your app faster while decreasing
# the load on computing resources


print(get_settings().base_url)
print(get_settings().db_url)