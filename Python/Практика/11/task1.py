import math

"""
(15 баллов) Напишите функцию, которая по 3 сторонам треугольника вычисляет его площадь.
Параметрами функции являются длины сторон треугольника.
Функция возвращает число (площадь).
Если треугольник с заданными сторонами не существует, то – 0. 
"""


def triangle(input_tuple):
    # Стороны треугольника
    a, b, c = input_tuple

    # Если сумма сторон меньше или равно третьей, то такого треугольника не существует
    if a + b <= c or a + c <= b or b + c <= a:
        return 0

    # Полупериметр
    p = sum(input_tuple) / 2

    # Площадь
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # Возврат значния
    return s


if __name__ == "__main__":
    result = triangle((6, 4, 5))
    print(result)
