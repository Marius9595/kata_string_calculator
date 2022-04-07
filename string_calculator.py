import unittest

class StringCalculator:

    def add(self, numbers):
        return 0


"""
input  ->  output

 ""    ->   0

 "1"   ->   1
 "2"   ->   2
 
 "1,2" ->   3

"""

#StringCalculatorShould
# red: 🔴
# green:🟢
class StringCalculatorShould(unittest.TestCase):

    def setUp(self) -> None:
        self.string_calculator = StringCalculator()

    def test_translate_empties_as_number(self):
        self.assertEqual(0, self.string_calculator.add(""))

    def test_work_with_a_single_number(self):
        self.assertEqual(1, self.string_calculator.add("1"))
        self.assertEqual(2, self.string_calculator.add("2"))


if __name__ == '__main__':
    unittest.main()
