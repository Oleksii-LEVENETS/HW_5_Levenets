"""
Task 1.
1. Реалізуйте три ролі користувачів групи соцмереж (Admin, Moderator, Member).
Об`єкти вcіх ролей повинні мати такі однакові атрибути – name, surname, age, join_date, user_id.
Модератор і адмін мають додатково атрибут badge (значок, або щось типу статусу, по суті просто текст).
Адмін має додатковий атрибут level.
Також у всіх повинна бути можливість отримати full_name – (name + surname).
name, surname, age, join_date – заповнюються при створені, приходять як аргументи в конструктор.
badge – опціонально.
level – відразу ставиться в значення 1, але можна змінювати після створення.
Всі користувачі можуть змінювати своє name, surname, age, badge (адмін і модератор) і level(для адміна).
join_date, user_id – змінювати забороняється будь-кому.
"""
import uuid


class Member:
    def __init__(self, name, surname, age, join_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.__join_date = join_date
        self.__user_id = uuid.uuid4()

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    full_name = property(fget=get_full_name)

    @property
    def join_date(self):
        join_date = self.__join_date
        return join_date

    @property
    def user_id(self):
        user_id = self.__user_id
        return user_id

    def __str__(self):  # Використовується у Moderator:  print(f"A New Moderator '{self}' created:"...
        return f"{self.name} {self.surname}"

    def __int__(self):  # Використовується у Moderator:  print(f" ..., age: '{int(self)}'...
        return self.age


class Moderator(Member):
    def __init__(self, name, surname, age, join_date, badge):
        super(Moderator, self).__init__(name, surname, age, join_date)
        self.badge = badge


class Admin(Moderator):
    def __init__(self, name, surname, age, join_date, badge, level=1):
        super(Admin, self).__init__(name, surname, age, join_date, badge)
        self.level = level
