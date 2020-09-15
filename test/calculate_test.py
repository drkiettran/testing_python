import unittest
from app.calculate import Calculate, main


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.add(2, 3))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")
        
    def test_main(self):
        self.assertTrue(main())


if __name__ == '__main__':
    unittest.main()
