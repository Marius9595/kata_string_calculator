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

#StringCalculatorShould test_translate_empties
# red: 🔴
# green:🟢
class StringCalculatorShould(unittest.TestCase):

    def setUp(self) -> None:
        self.string_calculator = StringCalculator()

    def test_translate_empties(self):
        self.assertEqual(0, self.string_calculator.add(""))  # add assertion here


if __name__ == '__main__':
    unittest.main()
