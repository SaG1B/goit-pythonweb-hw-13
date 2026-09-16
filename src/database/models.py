from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    avatar = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    confirmed = Column(Boolean, default=False)

class Contact(Base):
    __tablename__ = 'contacts'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)
    birthday = Column(Date, nullable=True)
    additional_data = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship('User', backref='contacts')
