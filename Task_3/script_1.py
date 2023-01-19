"""
Task_3
1. Реалізуйте клас вектора з трьома координатами.
Перегрузіть оператор + таким чином, щоб при додаванні двох векторів, утворювався новий вектор,
координатами якого буде сума відповідних координат.
Перегрузіть оператор *. При множені двох векторів, результатом буде число яке рахується по формулі –
сума добутків відповідних координат.
При додаванні або множені вектора на число (константу), всі координати додаються
або множаться на дане число відповідно.
Результатом додавання або множення вектора на число є новий вектор.
"""


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            num = self.x * other.x + self.y * other.y + self.z * other.z
            return num

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


print(Vector(1, 2, 3) + Vector(4, 5, 6))  # -> Vector(5, 7, 9)
print(Vector(1, 2, 3) + 1)  # -> Vector(2, 3, 4)
print(Vector(1, 2, 3) * 2)  # -> Vector(2, 4, 6)
assert Vector(1, 2, 3) * Vector(4, 5, 6) == 4 + 10 + 18 == 32
