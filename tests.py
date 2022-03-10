import numpy as np
import unittest

from main import AXES, Axis, DH_Transformation_Matrix
from main import FK
from main import rot
from main import Transformation_Matrix

ROTATION_SLICE = 100
class Test_rot(unittest.TestCase):
    def rot_helper(self, axis: Axis) -> None:
        for i in range(0, ROTATION_SLICE + 1):
            theta = 2 * i * np.pi / ROTATION_SLICE

            crot = np.cos(theta)
            srot = np.sin(theta)
            
            if axis == Axis.X:
                expected = np.array([
                    1, 0, 0,
                    0, crot, -srot,
                    0, srot, crot
                ]).reshape((AXES, AXES))
            elif axis == Axis.Y:
                expected = np.array([
                    crot, 0, srot,
                    0, 1, 0,
                    -srot, 0, crot
                ]).reshape((AXES, AXES))
            elif axis == Axis.Z:
                expected = np.array([
                    crot, -srot, 0,
                    srot, crot, 0,
                    0, 0, 1
                ]).reshape((AXES, AXES))
            else:
                expected = np.empty((AXES, AXES))

            self.assertTrue(np.array_equal(expected, rot(axis, theta)))

    def test_rot_x(self):
        self.rot_helper(Axis.X)

    def test_rot_y(self):
        self.rot_helper(Axis.Y)

    def test_rot_z(self):
        self.rot_helper(Axis.Z)

class Test_Transformation_Matrix(unittest.TestCase):
    pass

class Test_DH_Transformation_Matrix(unittest.TestCase):
    pass

class Test_FK(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()