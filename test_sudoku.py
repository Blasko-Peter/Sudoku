import sudoku
import unittest


class TestSudoku(unittest.TestCase):


    def test_check_result01(self):
        result = sudoku.check_result([[0,1,2],[1,2,3]], 0, 1, 1)
        self.assertEqual(result, 1)
    

    def test_check_result02(self):
        result = sudoku.check_result([[0,1,2],[1,2,3]], 0, 1, 5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
