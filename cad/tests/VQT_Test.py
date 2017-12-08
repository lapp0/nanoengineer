
import unittest
from VQT import angleBetween
import numpy as np


class GeometryFunctionsTestCase(unittest.TestCase):
    """Unit tests for the geometry functions defined in VQT.py"""

    def setUp(self):
        """Sets up any objects needed by this test case."""
        pass

    def tearDown(self):
        """Releases any resources used by this test case."""
        pass

    def testAngleBetween(self):
        vector1 = np.array((1, 0, 0))
        vector2 = np.array((0, 1, 0))
        angle = angleBetween(vector1, vector2)
        assert angle == 90, "Fails sanity check"
        assert np.all(vector1 == np.array((1, 0, 0))) and \
               np.all(vector2 == np.array((0, 1, 0))), \
               "Arguments were modified (recurrence of bug ####)"


if __name__ == "__main__":
    unittest.main()  # Run all tests whose names begin with 'test'
