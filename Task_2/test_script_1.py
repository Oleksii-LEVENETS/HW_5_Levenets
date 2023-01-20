"""
Task_2
1. Напишіть юніт-тести для Task1 використовуючи unittest.
Обов'язково протестуйте зміну значень атрибутів, а також розмежування доступу до функцій з додаткового файлу.
Перевірте, щоб юзер який має доступ до функції успішно виконав виклик, а юзер який доступу не має — отримав ексепшин.
"""
import uuid
from unittest import TestCase

from Task_1.script_1 import Admin, Member, Moderator
from Task_1.script_2 import NoAccess, create_article, delete_article, delete_group, \
     set_like_to_article, share_article, update_article


class TestUsers(TestCase):
    params = {
        "name": "Us",
        "surname": "Usenko",
        "age": 10,
        "join_date": "01-01-2023",
    }

    change = {
        "name": "Us_1",
        "surname": "Usenko_1",
        "age": 110,
        "join_date": "02-02-2023",
    }

    def setUp(self) -> None:
        self.member_1 = Member(**self.params)
        self.moderator_1 = Moderator(badge="Badge_Moderator", **self.params)
        self.admin_1 = Admin(badge="Badge_Admin", **self.params)

    def tearDown(self) -> None:
        self.member_1 = None
        self.moderator_1 = None
        self.admin_1 = None

# Member: create, change, access
    def test_create_member(self):
        self.assertEqual(self.member_1.name, self.params["name"])
        self.assertEqual(self.member_1.surname, self.params["surname"])
        self.assertEqual(self.member_1.age, self.params["age"])
        self.assertEqual(self.member_1.join_date, self.params["join_date"])
        with self.assertRaises(AttributeError):
            self.member_1.badge
        with self.assertRaises(AttributeError):
            self.member_1.level
        self.assertIsInstance(self.member_1.user_id, uuid.UUID)
        self.assertEqual(self.member_1.full_name, f"{self.params['name']} {self.params['surname']}")

    def test_change_member(self):
        member_1 = Member(**self.change)

        self.assertEqual(member_1.name, self.change["name"])
        self.assertEqual(member_1.surname, self.change["surname"])
        self.assertEqual(member_1.age, self.change["age"])
        with self.assertRaises(AttributeError):
            member_1.join_date = self.change["join_date"]
        with self.assertRaises(AttributeError):
            member_1.user_id = "1234"

        self.assertIsInstance(member_1.user_id, uuid.UUID)
        self.assertEqual(member_1.full_name, f"{self.change['name']} {self.change['surname']}")

    def test_access_member(self):
        self.assertEqual(set_like_to_article(self.member_1, 1), True)
        self.assertEqual(share_article(self.member_1, 1), True)
        with self.assertRaises(NoAccess):
            create_article(self.member_1, 1)
        with self.assertRaises(NoAccess):
            update_article(self.member_1, 1)
        with self.assertRaises(NoAccess):
            delete_article(self.member_1, 1)
        with self.assertRaises(NoAccess):
            delete_group(self.member_1, 1)

# Moderator: create, change, access
    def test_create_moderator(self):
        self.assertEqual(self.moderator_1.name, self.params["name"])
        self.assertEqual(self.moderator_1.surname, self.params["surname"])
        self.assertEqual(self.moderator_1.age, self.params["age"])
        self.assertEqual(self.moderator_1.join_date, self.params["join_date"])
        self.assertEqual(self.moderator_1.badge, "Badge_Moderator")
        with self.assertRaises(AttributeError):
            self.moderator_1.level
        self.assertIsInstance(self.moderator_1.user_id, uuid.UUID)
        self.assertEqual(self.moderator_1.full_name, f"{self.params['name']} {self.params['surname']}")

    def test_change_moderator(self):
        moderator_1 = Moderator(badge="New_Badge_Moderator", **self.change)

        self.assertEqual(moderator_1.name, self.change["name"])
        self.assertEqual(moderator_1.surname, self.change["surname"])
        self.assertEqual(moderator_1.age, self.change["age"])
        with self.assertRaises(AttributeError):
            moderator_1.join_date = self.change["join_date"]
        self.assertEqual(moderator_1.badge, "New_Badge_Moderator")
        with self.assertRaises(AttributeError):
            moderator_1.user_id = "1234"

        self.assertIsInstance(moderator_1.user_id, uuid.UUID)
        self.assertEqual(moderator_1.full_name, f"{self.change['name']} {self.change['surname']}")

    def test_access_moderator(self):
        self.assertEqual(set_like_to_article(self.moderator_1, 1), True)
        self.assertEqual(share_article(self.moderator_1, 1), True)
        self.assertEqual(create_article(self.moderator_1, 1), True)
        self.assertEqual(update_article(self.moderator_1, 1), True)
        with self.assertRaises(NoAccess):
            delete_article(self.moderator_1, 1)
        with self.assertRaises(NoAccess):
            delete_group(self.moderator_1, 1)

# Admin: create, change, access
    def test_create_admin(self):
        self.assertEqual(self.admin_1.name, self.params["name"])
        self.assertEqual(self.admin_1.surname, self.params["surname"])
        self.assertEqual(self.admin_1.age, self.params["age"])
        self.assertEqual(self.admin_1.join_date, self.params["join_date"])
        self.assertEqual(self.admin_1.badge, "Badge_Admin")
        self.assertEqual(self.admin_1.level, 1)
        self.assertIsInstance(self.admin_1.user_id, uuid.UUID)
        self.assertEqual(self.admin_1.full_name, f"{self.params['name']} {self.params['surname']}")

    def test_change_admin(self):
        admin_1 = Admin(badge="New_Badge_Admin", **self.change)

        self.assertEqual(admin_1.name, self.change["name"])
        self.assertEqual(admin_1.surname, self.change["surname"])
        self.assertEqual(admin_1.age, self.change["age"])
        self.assertEqual(admin_1.badge, "New_Badge_Admin")
        admin_1.level = 3
        self.assertEqual(admin_1.level, 3)
        with self.assertRaises(AttributeError):
            admin_1.join_date = self.change["join_date"]
        with self.assertRaises(AttributeError):
            admin_1.user_id = "1234"

        self.assertIsInstance(admin_1.user_id, uuid.UUID)
        self.assertEqual(admin_1.full_name, f"{self.change['name']} {self.change['surname']}")

    def test_access_admin(self):
        self.assertEqual(set_like_to_article(self.admin_1, 1), True)
        self.assertEqual(share_article(self.admin_1, 1), True)
        self.assertEqual(create_article(self.admin_1, 1), True)
        self.assertEqual(update_article(self.admin_1, 1), True)
        self.assertEqual(delete_article(self.admin_1, 1), True)
        with self.assertRaises(NoAccess):  # admin_1.level = 1
            delete_group(self.admin_1, 1)
        self.admin_1.level = 2
        with self.assertRaises(NoAccess):  # admin_1.level = 2
            delete_group(self.admin_1, 1)
        self.admin_1.level = 3
        self.assertEqual(delete_group(self.admin_1, 1), True)  # admin_1.level = 3
        self.admin_1.level = 4
        self.assertEqual(delete_group(self.admin_1, 1), True)  # admin_1.level = 4
