from typing import Tuple
import unittest

from mini_max.mini_max_sum import min_max, min_min

class TestMiniMaxSum(unittest.TestCase):

    def test_scenery_one(self):
        values = [1,3,5,7,9]
        self.assertAlmostEqual(min_max(values), 24)
        self.assertAlmostEqual(min_min(values), 16)