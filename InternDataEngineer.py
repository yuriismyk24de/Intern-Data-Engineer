import math

class Geometry:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        # Полупериметр треугольника
        s = (side1 + side2 + side3) / 2
        # Формула Герона для вычисления площади треугольника
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        # Проверяем, удовлетворяет ли треугольник теореме Пифагора
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

# Добавление других фигур легко осуществимо путем добавления новых методов в класс Geometry

# Юнит-тесты
import unittest

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Geometry.circle_area(3), 28.274333882308138)

    def test_triangle_area(self):
        self.assertAlmostEqual(Geometry.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(Geometry.is_right_triangle(3, 4, 5))

if __name__ == '__main__':
    unittest.main()
