# HW_5_Levenets
=================
ДЗ 5. HW5
Створено: 11.12.2022 13:58
Заняття 11. Тестування
----------------------
Task 1
1. Реалізуйте три ролі користувачів групи соцмереж (Admin, Moderator, Member).
Об`єкти віх ролей повинні мати такі однакові атрибути – name, surname, age, join_date, user_id.
Модератор і адмін мають додатково атрибут badge (значок, або щось типу статусу, по суті просто текст).
Адмін має додатковий атрибут level.
Також у всіх повинна бути можливість отримати full_name – (name + surname). name, surname, age, join_date – 
заповнюються при створені, приходять як аргументи в конструктор. badge – опціонально. Level – відразу ставиться 
в значення 1, але можна змінювати після створення Всі користувачі можуть змінювати своє name, surname, age,
badge(адмін і модератор) і level(для адміна). join_date, user_id – змінювати забороняється будь-кому.

2. В файлі hw_data.py лежать «заглушки» функцій для роботи в групі. Реалізуйте розмежування доступу.
Якщо доступ заборонений – згенеруйте ексепшин NoAccess (створіть даний ексепшин).
Member – може ставити лайк, і шейрити статтю
Moderator – те ж що і Member, + створювати і оновлювати статтю Admin – те ж що і Moderator+ видаляти статтю
і видаляти групу.
Проте видаляти групу може адміністратор рівня не менше ніж 3
Для реалізації розмежування ви можете дописувати функції, проте найкращим варіантом буде реалізувати перевірку
на доступ через декоратори.
----------------------
Task 2
1. Напишіть юніт тести для Task1 використовуючи unittest. Обовязково протестуйте зміну значень атрибутів, 
а також розмежування доступу до функцій з додаткового файлу. Перевірте щоб юзер який має доступ до функції
успішно виконав виклик, а юзер який доступу не має — отримав ексепшин
2. Теж саме тільки використовуючи pytest
---------------------
Task 3
1. Реалізуйте клас вектора з трьома координатами.
Перегрузіть оператор + таким чином, щоб при додаванні двох векторів, утворювався новий вектор, 
координатами якого буде сума відповідних координат.
Перегрузіть оператор *. При множені двох векторів, результатом буде число яке рахується по формулі 
– сума добутків відповідних координат.
При додаванні або множені вектора на число (константу), всі координати додаються або множаться 
на дане число відповідно. Результатом додавання або множення вектора на число є новий вектор.
---------------------