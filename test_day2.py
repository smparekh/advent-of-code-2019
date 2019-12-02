import unittest

from day2 import run


class MyTestCase(unittest.TestCase):
    def test_case0(self):
        inputs = [1, 0, 0, 0, 99]
        outputs = run(inputs)
        print(outputs)
        self.assertListEqual([2, 0, 0, 0, 99], outputs)

    def test_case00(self):
        inputs = [2, 3, 0, 3, 99]
        outputs = run(inputs)
        print(outputs)
        self.assertListEqual([2, 3, 0, 6, 99], outputs)

    def test_case1(self):
        inputs = [2, 4, 4, 5, 99, 0]
        outputs = run(inputs)
        print(outputs)
        self.assertListEqual([2, 4, 4, 5, 99, 9801], outputs)

    def test_case2(self):
        inputs = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        outputs = run(inputs)
        print(outputs)
        self.assertListEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], outputs)


if __name__ == '__main__':
    unittest.main()
