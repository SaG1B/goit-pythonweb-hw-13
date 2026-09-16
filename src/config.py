import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_URL: str = os.getenv("DB_URL", "postgresql+pg8000://postgres:SagibPython@localhost:5432/contacts_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "Sagibpython")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", "")
    MAIL_FROM: str = os.getenv("MAIL_FROM", "")
    MAIL_PORT: int = int(os.getenv("MAIL_PORT", 587))
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_STARTTLS: bool = os.getenv("MAIL_STARTTLS", "True") == "True"
    MAIL_SSL_TLS: bool = os.getenv("MAIL_SSL_TLS", "False") == "False"
    USE_CREDENTIALS: bool = os.getenv("USE_CREDENTIALS", "True") == "True"
    VALIDATE_CERTS: bool = os.getenv("VALIDATE_CERTS", "True") == "True"

settings = Settings()