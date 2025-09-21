from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    database_url: str = Field(default="postgresql+psycopg://itc:itc@db:5432/itc", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://redis:6379/0", alias="REDIS_URL")
    aws_region: str = Field(default="us-west-1", alias="AWS_REGION")
    aws_bucket: str = Field(default="peninsulators-itc-dev", alias="AWS_S3_BUCKET")
    trello_key: str = Field(default="", alias="TRELLO_KEY")
    trello_token: str = Field(default="", alias="TRELLO_TOKEN")
    bc_api_key: str = Field(default="", alias="BC_API_KEY")
    zoom_client_id: str = Field(default="", alias="ZOOM_CLIENT_ID")
    zoom_client_secret: str = Field(default="", alias="ZOOM_CLIENT_SECRET")
    deep_email_cap: int = Field(default=200, alias="DEEP_EMAIL_CAP")
    max_attachment_mb: int = Field(default=200, alias="MAX_ATTACHMENT_MB")
    timezone: str = Field(default="America/Los_Angeles", alias="TIMEZONE")
    allowlist_inboxes: List[str] = Field(default=["mpansegrau@peninsulators.com","bids@peninsulators.com","contracts@peninsulators.com"], alias="ALLOWLIST_INBOXES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True

settings = Settings()
