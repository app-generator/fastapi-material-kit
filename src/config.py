from pydantic import BaseSettings
from secrets import token_hex

class Settings(BaseSettings):
    secret_key: str = token_hex(12)
    algorithm: str = 'HS256'
    debugging: bool = True
    access_token_expire_minutes: int = 60*2 #2 hours

    github_secret_key: str = None
    github_is_active: bool = False
    github_client_id: str = None

    def __init__(self):
        super().__init__()
        self.check_github()

    def check_github(self):
        if self.github_secret_key and self.github_client_id:
            self.github_is_active = True



    class Config:
        env_file = "./.env"



settings = Settings()