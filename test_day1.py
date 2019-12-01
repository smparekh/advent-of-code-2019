import unittest
from day1 import module_fuel_required, total_fuel_required_part2


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(33583, module_fuel_required(100756))

    def test_case_2(self):
        self.assertEqual(654, module_fuel_required(1969))

    def test_case_3(self):
        self.assertEqual(50346, total_fuel_required_part2([100756]))

    def test_case_4(self):
        self.assertEqual(966, total_fuel_required_part2([1969]))

    def test_case_5(self):
        self.assertEqual(51312, total_fuel_required_part2([1969, 100756]))


if __name__ == '__main__':
    unittest.main()
