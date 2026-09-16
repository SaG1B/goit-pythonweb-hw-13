from jose import jwt
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr
from src.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME="Contacts App",
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS
)

def create_email_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

async def send_email(email: EmailStr, username: str, host: str):
    try:
        token_verification = create_email_token({"sub": email})
        message = MessageSchema(
            subject="Подтвердите ваш email",
            recipients=[email],
            body=f"<html><body><p>Здравствуйте, {username}!</p><p>Для подтверждения вашей учетной записи перейдите по ссылке:</p><a href='{host}api/auth/confirmed_email/{token_verification}'>Подтвердить email</a></body></html>",
            subtype=MessageType.html
        )
        fm = FastMail(conf)
        await fm.send_message(message)
    except ConnectionErrors as err:
        print(err)
