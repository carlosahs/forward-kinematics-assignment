import numpy as np

from enum import Enum
from typing import List
from typing import Tuple
from typing_extensions import Self

class Axis(Enum):
    X = 'x'
    Y = 'y'
    Z = 'z'

Vector = List[float]

class Translation_Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        # 3 by 1 vector
        self.vector = np.array([x, y, z]).reshape(3, 1)

class Rotation_Matrix:
    def __init__(self, axis: Axis) -> None:
        self.axis = axis
        self.matrix = np.identity(3)

    def rot(self, rad: float) -> None:
        crot = np.cos(rad)
        srot = np.sin(rad)

        if self.axis == Axis.X:
            self.matrix[1][1] = crot
            self.matrix[2][2] = crot

            self.matrix[1][2] = -srot
            self.matrix[2][1] = srot
        elif self.axis == Axis.Y:
            self.matrix[0][0] = crot
            self.matrix[2][2] = crot

            self.matrix[2][0] = -srot
            self.matrix[0][2] = srot
        elif self.axis == Axis.Z:
            self.matrix[0][0] = crot
            self.matrix[1][1] = crot

            self.matrix[0][1] = -srot
            self.matrix[1][0] = srot

class Transformation_Matrix:
    def __init__(self, rmatrix: Rotation_Matrix, tvector: Translation_Vector) -> None:
        self.rmatrix = rmatrix
        self.tvector = tvector

def FK(L: Vector, q: Vector) -> Vector:
    """
    Solves the forward kinematics of a planar 2R robot.

    Returns:
        @P (Vector): 2 by 1 vector containing the end effector's x and y 
            coordinates expressed in the base frame.
    """

    P = []

    return P

if __name__ == '__main__':
    # TODO
    pass