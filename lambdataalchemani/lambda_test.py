"""

"""

import unittest

from example_module import COLORS, increment

class ExampleTest(unittest.TestCase):
    """
    #TODO
    """
    def test_increment(self):
        x0 = 0
        y0 = increment(x0) #y0 == 1
        self.assertEqual(y0, 1)
    
        x1 = 100
        y1 = increment(x1) #y1 == 101
        self.assertEqual(y1, 101)

