import operator
import unittest
from functools import reduce

class StringCalculator:

    def add(self, numbers):

        if(numbers == ''):
            return 0

        return int(reduce(lambda sum, number: int(sum)+int(number), list(numbers.split(','))))


"""
input  ->  output

 ""    ->   0

 "1"   ->   1
 "2"   ->   2
 
 "1,2" ->   3
 
 "1\n2,3" -> 6

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

    def test_add_all_numbers_identified(self):
        self.assertEqual(3, self.string_calculator.add("1,2"))
        self.assertEqual(14, self.string_calculator.add("5,9"))

    def test_handle_new_lines_between_numbers(self):
        self.assertEqual(3, self.string_calculator.add("1\n2,3"))


if __name__ == '__main__':
    unittest.main()
