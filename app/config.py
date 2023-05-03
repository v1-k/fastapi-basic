from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    rabbitmq_user: str
    rabbitmq_password: str
    rabbitmq_location: str
    rabbitmq_vhost: str

    class Config:
        env_file = ".env"


settings = Settings()
