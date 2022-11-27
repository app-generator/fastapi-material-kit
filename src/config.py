from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    debugging: int
    access_token_expire_minutes: int = 30

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