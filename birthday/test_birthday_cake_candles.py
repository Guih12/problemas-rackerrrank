import unittest

from birthday.birthday_cake_candles import birthdayCakeCandles

class TestBirthdayCakeCandles(unittest.TestCase):
    #should return 2
    def test_scenery_one(self):
        candles = [4, 4, 1, 3]
        self.assertAlmostEqual(birthdayCakeCandles(candles), 2)
    
    #should return 2
    def test_scenery_two(self):
         candles = [3, 2, 1, 3]
         self.assertAlmostEqual(birthdayCakeCandles(candles), 2)

    #should return 3
    def test_scenery_tree(self):
        candles = [3,2,1,3,3]
        self.assertAlmostEqual(birthdayCakeCandles(candles), 3)