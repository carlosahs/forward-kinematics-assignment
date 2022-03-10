import numpy as np
import unittest

from main import AXES, Axis, DH_Transformation_Matrix
from main import FK
from main import rot
from main import Transformation_Matrix

ROTATION_SLICE = 100
class Test_rot(unittest.TestCase):
    def test_rot_x(self):
        # Test every hundreth of a full rotation
        for i in range(0, ROTATION_SLICE + 1):
            theta = 2 * i * np.pi / ROTATION_SLICE

            crot = np.cos(theta)
            srot = np.sin(theta)
            
            expected = np.array([
                1, 0, 0,
                0, crot, -srot,
                0, srot, crot
            ]).reshape((AXES, AXES))

            self.assertTrue(np.array_equal(expected, rot(Axis.X, theta)))

class Test_Transformation_Matrix(unittest.TestCase):
    pass

class Test_DH_Transformation_Matrix(unittest.TestCase):
    pass

class Test_FK(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()