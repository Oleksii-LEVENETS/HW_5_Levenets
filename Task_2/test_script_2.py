"""
Task_2
2. Теж саме тільки використовуючи pytest
-----------------------------------------
1. Напишіть юніт тести для Task1 використовуючи unittest.
Обов'язково протестуйте зміну значень атрибутів, а також розмежування доступу до функцій з додаткового файлу.
Перевірте, щоб юзер який має доступ до функції успішно виконав виклик, а юзер який доступу не має — отримав ексепшин.
"""

import uuid

import pytest

from HW_5_Levenets.HW_5_Levenets.Task_1.script_1 import Admin, Moderator, Member
from HW_5_Levenets.HW_5_Levenets.Task_1.script_2 import set_like_to_article, share_article, create_article, \
    update_article, delete_article, delete_group, NoAccess

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


# Member: create, change, access
def test_create_member():
    member_1 = Member(**params)
    assert member_1.name == params["name"]
    assert member_1.surname == params["surname"]
    assert member_1.join_date == params["join_date"]
    # assert isinstance(member_1.badge, AttributeError)
    with pytest.raises(AttributeError):
        member_1.badge
    with pytest.raises(AttributeError):
        member_1.level
    assert isinstance(member_1.user_id, uuid.UUID)
    assert member_1.full_name == f"{params['name']} {params['surname']}"


def test_change_member():
    member_1 = Member(**change)
    assert member_1.name == change["name"]
    assert member_1.surname == change["surname"]
    assert member_1.age == change["age"]
    with pytest.raises(AttributeError):
        member_1.join_date = change["join_date"]
    with pytest.raises(AttributeError):
        member_1.user_id = "1234"

    assert isinstance(member_1.user_id, uuid.UUID)
    assert member_1.full_name == f"{change['name']} {change['surname']}"


def test_access_member():
    member_1 = Member(**params)
    assert set_like_to_article(member_1, 1) is None
    assert share_article(member_1, 1) is None
    with pytest.raises(NoAccess):
        create_article(member_1, 1)
    with pytest.raises(NoAccess):
        update_article(member_1, 1)
    with pytest.raises(NoAccess):
        delete_article(member_1, 1)
    with pytest.raises(NoAccess):
        delete_group(member_1, 1)


# Moderator: create, change, access
def test_create_moderator():
    moderator_1 = Moderator(badge="Badge_Moderator", **params)
    assert moderator_1.name == params["name"]
    assert moderator_1.surname == params["surname"]
    assert moderator_1.age == params["age"]
    assert moderator_1.join_date == params["join_date"]
    assert moderator_1.badge == "Badge_Moderator"
    with pytest.raises(AttributeError):
        moderator_1.level
    assert isinstance(moderator_1.user_id, uuid.UUID)
    assert moderator_1.full_name == f"{params['name']} {params['surname']}"


def test_change_moderator():
    moderator_1 = Moderator(badge="New_Badge_Moderator", **change)
    assert moderator_1.name == change["name"]
    assert moderator_1.surname == change["surname"]
    assert moderator_1.age == change["age"]
    with pytest.raises(AttributeError):
        moderator_1.join_date = change["join_date"]
    assert moderator_1.badge == "New_Badge_Moderator"
    with pytest.raises(AttributeError):
        moderator_1.user_id = "1234"

    assert isinstance(moderator_1.user_id, uuid.UUID)
    assert moderator_1.full_name == f"{change['name']} {change['surname']}"


def test_access_moderator():
    moderator_1 = Moderator(badge="New_Badge_Moderator", **change)
    assert set_like_to_article(moderator_1, 1) is None
    assert share_article(moderator_1, 1) is None
    assert create_article(moderator_1, 1) is None
    assert update_article(moderator_1, 1) is None
    with pytest.raises(NoAccess):
        delete_article(moderator_1, 1)
    with pytest.raises(NoAccess):
        delete_group(moderator_1, 1)


# Admin: create, change, access
def test_create_admin():
    admin_1 = Admin(badge="Badge_Admin", **params)
    assert admin_1.name == params["name"]
    assert admin_1.surname == params["surname"]
    assert admin_1.age == params["age"]
    assert admin_1.join_date == params["join_date"]
    assert admin_1.badge == "Badge_Admin"
    assert admin_1.level == 1
    assert isinstance(admin_1.user_id, uuid.UUID)
    assert admin_1.full_name == f"{params['name']} {params['surname']}"


def test_change_admin():
    admin_1 = Admin(badge="New_Badge_Admin", **change)
    assert admin_1.name == change["name"]
    assert admin_1.surname == change["surname"]
    assert admin_1.age == change["age"]
    assert admin_1.badge == "New_Badge_Admin"
    admin_1.level = 3
    assert admin_1.level == 3
    with pytest.raises(AttributeError):
        admin_1.join_date = change["join_date"]
    with pytest.raises(AttributeError):
        admin_1.user_id = "1234"

    assert isinstance(admin_1.user_id, uuid.UUID)
    assert admin_1.full_name == f"{change['name']} {change['surname']}"


def test_access_admin():
    admin_1 = Admin(badge="Badge_Admin", **params)
    assert set_like_to_article(admin_1, 1) is None
    assert share_article(admin_1, 1) is None
    assert create_article(admin_1, 1) is None
    assert update_article(admin_1, 1) is None
    assert delete_article(admin_1, 1) is None
    with pytest.raises(NoAccess):  # admin_1.level = 1
        delete_group(admin_1, 1)
    admin_1.level = 2
    with pytest.raises(NoAccess):  # admin_1.level = 2
        delete_group(admin_1, 1)
    admin_1.level = 3
    assert delete_group(admin_1, 1) is None  # admin_1.level = 3
    admin_1.level = 4
    assert delete_group(admin_1, 1) is None  # admin_1.level = 4
