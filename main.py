import numpy as np

from enum import Enum
from typing import List
from typing import Tuple
from typing_extensions import Self

AXES = 3

class Axis(Enum):
    X = 'x'
    Y = 'y'
    Z = 'z'

def rot(axis: Axis, rad: float) -> np.ndarray:
    crot = np.cos(rad)
    srot = np.sin(rad)

    mat = np.identity(AXES)

    if axis == Axis.X:
        mat[1][1] = crot
        mat[2][2] = crot

        mat[1][2] = -srot
        mat[2][1] = srot
    elif axis == Axis.Y:
        mat[0][0] = crot
        mat[2][2] = crot

        mat[2][0] = -srot
        mat[0][2] = srot
    elif axis == Axis.Z:
        mat[0][0] = crot
        mat[1][1] = crot

        mat[0][1] = -srot
        mat[1][0] = srot

    mat

class Transformation_Matrix:
    def __init__(self, rmatrix: np.ndarray, tvector: np.ndarray) -> None:
        assert rmatrix.shape == (AXES, AXES)
        assert tvector.shape == (AXES, 1)

        self.rmatrix = rmatrix
        self.tvector = tvector

    def mul(self, tmatrix: Self) -> Self:
        return Transformation_Matrix(
            np.matmul(self.rmatrix, tmatrix.rmatrix),
            np.matmul(self.rmatrix, self.tvector) + tmatrix.tvector
        )

    def inv(self) -> Self:
        return Transformation_Matrix(
            self.rmatrix.transpose(),
            np.matmul(-self.rmatrix.transpose(), self.tvector)
        ) 

def FK(L: Tuple[int, int], q: Tuple[int, int]) -> Tuple[int, int]:
    """
    Solves the forward kinematics of a planar 2R robot.

    Returns:
        @P (Tuple[int, int]): 2 by 1 vector containing the end effector's x and y 
            coordinates expressed in the base frame.
    """

    q_sum = sum(q)

    L1 = L[0]
    L2 = L[1]

    q1 = q[0]

    P = (
        L1 * np.cos(q_sum) + L1 * np.cos(q1),
        L2 * np.sin(q_sum) + L2 * np.sin(q1)
    )

    return P

def GENFK(
    a: np.ndarray, alpha: np.ndarray, d: np.ndarray, 
    theta: np.ndarray, sigma: bool
) -> Transformation_Matrix:
    pass

def plot_FK(L: Tuple[int, int], q: Tuple[int, int], fk: Tuple[int, int]) -> None:
    pass

def rot2euler(R):
    pass

def euler2rot(A):
    pass

def rot2quat(R):
    pass

def quat2rot(Q):
    pass

if __name__ == '__main__':
    # TODO
    pass