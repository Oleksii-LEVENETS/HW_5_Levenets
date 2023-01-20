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

1.2 Ваш декоратор не повертає результат виконання функції яку він декорує
даний декоратор не добре реалізований, виходить що ви двічі реєструйєте його для функції,
один раз коли призначаєте на функцію, другий раз в самому декораторі записуючи імя функції.
+ воно може не спрацювати як потрібно, якщо на функції будуть ще декоратори,
тоді вам func.__name__ поверне імя іншого декоратора (якщо ви не перевизначите це імя, а в більшості випадків
цього не роблять)
подумайте над тим щоб цей декоратор змінити на декоратор в "3 рівні"
це може виглядати таким чином
@check_access(roles=[Member, Moderator])
таким чином вам потрібно буде в середині перевірити чи юзер є екземпляром одного з класів заданих в roles
також такий декоратор ви можете назначити на будь-яку функцію, змінюючи тільки перелік ролей кому доступна цю функція

"""
from Task_1.script_1 import Admin, Member, Moderator


class NoAccess(Exception):
    pass


def check_access(roles):
    def decor(func):
        def wrap(user, *args):
            if isinstance(user, roles):
                return func(user, *args)
            else:
                raise NoAccess
        return wrap
    return decor


def check_access_level(roles, level):
    def decor(func):
        def wrap(user, *args):
            if isinstance(user, roles) and user.level >= level:
                return func(user, *args)
            else:
                raise NoAccess
        return wrap
    return decor


@check_access_level(roles=(Admin,), level=3)
def delete_group(user, group_id):
    print("Group has been deleted")
    return True


@check_access(roles=(Admin, ))
def delete_article(user, article_id):
    print("Article has been deleted")
    return True


@check_access(roles=(Admin, Moderator))
def create_article(user, post_data):
    print("Article has been created")
    return True


@check_access(roles=(Admin, Moderator))
def update_article(user, update_data):
    print("Article has been updated")
    return True


@check_access(roles=(Admin, Member, Moderator))
def share_article(user, article_id):
    print("Article has been shared")
    return True


@check_access(roles=(Admin, Member, Moderator))
def set_like_to_article(user, post_data):
    print("Like has been set")
    return True
