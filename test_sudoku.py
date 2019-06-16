import sudoku
import unittest


class TestSudoku(unittest.TestCase):


    def test_database(self):
        result = sudoku.database()
        self.assertEqual(result, [
            ['4', '3', '9', '8', '6', '7', '2', '5', '1'],
            ['1', '7', '8', '5', '4', '2', '6', '3', '9'],
            ['6', '5', '2', '9', '3', '1', '8', '4', '7'],
            ['7', '4', '3', '1', '9', '8', '5', '6', '2'],
            ['5', '2', '6', '4', '7', '3', '1', '9', '8'],
            ['8', '9', '1', '6', '2', '5', '4', '7', '3'],
            ['3', '1', '7', '2', '5', '4', '9', '8', '6'],
            ['9', '8', '4', '3', '1', '6', '7', '2', '5'],
            ['2', '6', '5', '7', '8', '9', '3', '1', '4']
            ])


    def test_random_int(self):
        result = sudoku.random_int(0, 0)
        self.assertEqual(result, 0)


    def test_check_result01(self):
        result = sudoku.check_result([[0,1,2],[1,2,3]], 0, 1, 1)
        self.assertEqual(result, 1)
    

    def test_check_result02(self):
        result = sudoku.check_result([[0,1,2],[1,2,3]], 0, 1, 5)
        self.assertEqual(result, 0)
    

    def test_create_game_table01(self):
        result = sudoku.create_game_table([[0,1,2,3,4],[5,6,7,8,9]], 1, 0, 0)
        self.assertEqual(result, [[" ",1,2,3,4],[" ",6,7,8,9]])
    

    def test_create_game_table02(self):
        result = sudoku.create_game_table([[0,1,2,3,4],[5,6,7,8,9]], 2, 0, 2)
        self.assertEqual(result, [[" "," "," ",3,4],[" "," "," ",8,9]])
    

    def test_create_game_table03(self):
        result = sudoku.create_game_table([[0,1,2,3,4],[5,6,7,8,9]], 3, 0, 4)
        self.assertEqual(result, [[" "," "," "," "," "],[" "," "," "," "," "]])


if __name__ == "__main__":
    unittest.main()
