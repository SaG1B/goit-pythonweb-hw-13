from datetime import date, timedelta
from typing import List, Optional

from sqlalchemy import extract, or_
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel


async def get_contacts(
    skip: int, limit: int, user: User, db: Session
) -> List[Contact]:
    return (
        db.query(Contact)
        .filter(Contact.user_id == user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


async def get_contact(contact_id: int, user: User, db: Session) -> Optional[Contact]:
    return (
        db.query(Contact)
        .filter(Contact.id == contact_id, Contact.user_id == user.id)
        .first()
    )


async def create_contact(body: ContactModel, user: User, db: Session) -> Contact:
    contact = Contact(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        phone=body.phone,
        birthday=body.birthday,
        additional_data=body.additional_data,
        user=user,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(
    contact_id: int, body: ContactModel, user: User, db: Session
) -> Optional[Contact]:
    contact = await get_contact(contact_id, user, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.additional_data = body.additional_data
        db.commit()
    return contact


async def remove_contact(contact_id: int, user: User, db: Session) -> Optional[Contact]:
    contact = await get_contact(contact_id, user, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(
    query: str, skip: int, limit: int, user: User, db: Session
) -> List[Contact]:
    return (
        db.query(Contact)
        .filter(
            Contact.user_id == user.id,
            or_(
                Contact.first_name.ilike(f"%{query}%"),
                Contact.last_name.ilike(f"%{query}%"),
                Contact.email.ilike(f"%{query}%"),
            ),
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


async def get_upcoming_birthdays(user: User, db: Session) -> List[Contact]:
    today = date.today()
    upcoming = today + timedelta(days=7)
    
    contacts = db.query(Contact).filter(Contact.user_id == user.id).all()
    result = []
    
    for contact in contacts:
        if contact.birthday:
            bday_this_year = contact.birthday.replace(year=today.year)
            if today <= bday_this_year <= upcoming:
                result.append(contact)
                
    return result
