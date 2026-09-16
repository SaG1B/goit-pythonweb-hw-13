@'
from typing import List
from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import or_, extract

from src.database.models import Contact, User
from src.schemas import ContactModel

def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()

def get_contact(contact_id: int, user: User, db: Session) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == user.id).first()

def create_contact(body: ContactModel, user: User, db: Session) -> Contact:
    contact = Contact(**body.model_dump(), user_id=user.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def update_contact(contact_id: int, body: ContactModel, user: User, db: Session) -> Contact | None:
    contact = get_contact(contact_id, user, db)
    if contact:
        for key, value in body.model_dump().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact

def remove_contact(contact_id: int, user: User, db: Session) -> Contact | None:
    contact = get_contact(contact_id, user, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact

def search_contacts(query: str, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(
        Contact.user_id == user.id,
        or_(
            Contact.first_name.ilike(f"%{query}%"),
            Contact.last_name.ilike(f"%{query}%"),
            Contact.email.ilike(f"%{query}%")
        )
    ).all()

def get_upcoming_birthdays(user: User, db: Session) -> List[Contact]:
    today = date.today()
    next_week = today + timedelta(days=7)
    
    contacts = db.query(Contact).filter(Contact.user_id == user.id).all()
    result = []
    
    for contact in contacts:
        if contact.birthday:
            bday_this_year = contact.birthday.replace(year=today.year)
            if bday_this_year < today:
                bday_this_year = contact.birthday.replace(year=today.year + 1)
            
            if today <= bday_this_year <= next_week:
                result.append(contact)
                
    return result
'@ | Out-File -Encoding utf8 .\src\repository\contacts.py