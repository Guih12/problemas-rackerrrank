import unittest

from diagonal_diference import diagonalDiference


class TestDiagonalDiference(unittest.TestCase):

    #should return 15
    def test_scenare_one(self):
        matrix = [[1,2,3], [4,5,6], [7, 8, 9]]
        self.assertAlmostEqual(diagonalDiference(matrix), 0)
    
    #shold return 2
    def test_scenare_two(self):
        matrix = [[1,2,3], [4,5,6], [9, 8, 9]]
        self.assertAlmostEqual(diagonalDiference(matrix), 2)
    
    #shold return 15
    def test_scenare_tree(self):
        matrix = [[11,2,4], [4,5,6], [10, 8, -12]]
        self.assertAlmostEqual(diagonalDiference(matrix), 15)