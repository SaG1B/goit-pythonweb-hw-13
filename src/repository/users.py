from sqlalchemy.orm import Session
from src.database.models import User

def update_avatar(email: str, url: str, db: Session) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.avatar = url
        db.commit()
        db.refresh(user)
    return user
