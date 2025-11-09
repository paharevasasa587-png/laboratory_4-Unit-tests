import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    # Тесты для площади треугольника (area)
    def test_area_normal_values(self):
        """Тест площади с обычными значениями"""
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_area_zero_base(self):
        """Тест площади с нулевым основанием"""
        res = area(0, 7)
        self.assertEqual(res, 0)
    
    def test_area_zero_height(self):
        """Тест площади с нулевой высотой"""
        res = area(8, 0)
        self.assertEqual(res, 0)
    
    def test_area_fractional_values(self):
        """Тест площади с дробными значениями"""
        res = area(8.17, 6.13)
        self.assertAlmostEqual(res, 25.04105) 
    
    def test_area_large_numbers(self):
        """Тест площади с большими числами"""
        res = area(100, 50)
        self.assertEqual(res, 2500) 
    
    # Тесты для периметра треугольника (perimeter)
    def test_perimeter_normal_triangle(self):
        """Тест периметра обычного треугольника"""
        res = perimeter(7, 8, 9)
        self.assertEqual(res, 24)

    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_perimeter_right_triangle(self):
        """Тест периметра прямоугольного треугольника"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_zero_sides(self):
        """Тест периметра с нулевыми сторонами"""
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_fractional_sides(self):
        """Тест периметра с дробными сторонами"""
        res = perimeter(3.5, 4.5, 5.5)
        self.assertAlmostEqual(res, 13.5)
    
    def test_perimeter_large_numbers(self):
        """Тест периметра с большими числами"""
        res = perimeter(100, 150, 200)
        self.assertEqual(res, 450)
    
    def test_perimeter_negative_should_work(self):
        """Тест периметра с отрицательными значениями"""
        res  = perimeter(-3, -4, -5)
        self.assertEqual(res, -12)  