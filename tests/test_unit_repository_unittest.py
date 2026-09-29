import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from src.database.models import Contact, User
from src.repository.contacts import get_contacts, get_contact


class TestContactsRepositoryUnittest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1, email="test@example.com")

    async def test_get_contacts(self):
        contacts = [Contact(id=1, first_name="John", last_name="Doe")]
        self.session.query().filter().offset().limit().all.return_value = contacts

        result = await get_contacts(skip=0, limit=10, user=self.user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_get_contact_found(self):
        contact = Contact(id=1, first_name="John", last_name="Doe", user_id=self.user.id)
        self.session.query().filter().first.return_value = contact

        result = await get_contact(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)


if __name__ == "__main__":
    unittest.main()