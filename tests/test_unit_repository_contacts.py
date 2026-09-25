import unittest
from unittest.mock import MagicMock
from datetime import date

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel
from src.repository.contacts import (
    get_contacts,
    get_contact,
    create_contact,
    remove_contact,
)


class TestContactsRepository(unittest.TestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1, email="test@example.com")

    def test_get_contacts(self):
        contacts = [Contact(id=1), Contact(id=2)]
        self.session.query().filter().offset().limit().all.return_value = contacts
        result = get_contacts(skip=0, limit=10, user=self.user, db=self.session)
        self.assertEqual(result, contacts)

    def test_get_contact_found(self):
        contact = Contact(id=1, user_id=self.user.id)
        self.session.query().filter().first.return_value = contact
        result = get_contact(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    def test_get_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = get_contact(contact_id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    def test_create_contact(self):
        body = ContactModel(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="+380991112233",
            birthday=date(1990, 1, 1),
            additional_data="Friend",
        )
        result = create_contact(body=body, user=self.user, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.email, body.email)

    def test_remove_contact_found(self):
        contact = Contact(id=1, user_id=self.user.id)
        self.session.query().filter().first.return_value = contact
        result = remove_contact(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    def test_remove_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = remove_contact(contact_id=1, user=self.user, db=self.session)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()