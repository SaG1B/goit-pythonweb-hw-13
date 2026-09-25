import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(enum.Enum):
    admin: str = "admin"
    moderator: str = "moderator"
    user: str = "user"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    role = Column(Enum(Role), default=Role.user, nullable=False)
    confirmed = Column(Boolean, default=False)


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    phone = Column(String(20), nullable=False)
    birthday = Column(DateTime, nullable=False)
    additional_data = Column(String(250), nullable=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), default=None)
    user = relationship("User", backref="contacts")