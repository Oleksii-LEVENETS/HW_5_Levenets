"""
Task 1.
2. В файлі hw_data.py лежать «заглушки» функцій для роботи в групі. Реалізуйте розмежування доступу.
Якщо доступ заборонений – згенеруйте ексепшин NoAccess (створіть даний ексепшин).
Member – може ставити лайк, і шейрити статтю.
Moderator – те ж що і Member, + створювати і оновлювати статтю.
Admin – те ж що і Moderator + видаляти статтю і видаляти групу. Проте видаляти групу може адміністратор рівня
не менше ніж 3.
Для реалізації розмежування ви можете дописувати функції, проте найкращим варіантом буде реалізувати перевірку
на доступ через декоратори.
"""
from HW_5_Levenets.HW_5_Levenets.Task_1.script_1 import Admin, Member, Moderator


class NoAccess(Exception):
    pass


def decorator(func):
    def wrap(user, *args, **kwargs):
        member_list = ["set_like_to_article", "share_article"]
        moderator_list = ["set_like_to_article", "share_article", 'create_article', 'update_article']
        admin_list_1 = ["set_like_to_article", "share_article", 'create_article', 'update_article', 'delete_article']
        if isinstance(user, (Admin, Moderator, Member)) and (func.__name__ in member_list):
            func(user, *args, **kwargs)
        elif isinstance(user, (Admin, Moderator)) and func.__name__ in moderator_list:
            func(user, *args, **kwargs)
        elif isinstance(user, Admin) and func.__name__ in admin_list_1:
            func(user, *args, **kwargs)
        elif isinstance(user, Admin) and user.level >= 3:
            func(user, *args, **kwargs)
            # return func(user, *args, **kwargs)
        else:
            raise NoAccess("NoAccess")
    return wrap


@decorator
def delete_group(user, group_id):
    print("Group has been deleted")
    return True


@decorator
def delete_article(user, article_id):
    print("Article has been deleted")
    return True


@decorator
def create_article(user, post_data):
    print("Article has been created")
    return True


@decorator
def update_article(user, update_data):
    print("Article has been updated")
    return True


@decorator
def share_article(user, article_id):
    print("Article has been shared")
    return True


@decorator
def set_like_to_article(user, post_data):
    print("Like has been set")
    return True
