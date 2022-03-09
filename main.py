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
    def __init__(self) -> None:
        self.rmat = np.identity(AXES)
        self.tvec = np.zeros((AXES, 1))

    def rot(self, axis: Axis, rad: float) -> None:
        self.rmat = np.matmul(self.rmat, rot(axis, rad))

    def trans(self, x: float, y: float, z: float) -> None:  
        self.tvec[0] += x
        self.tvec[1] += y
        self.tvec[2] += z

    def mul(self, tmatrix: Self):
        self.rmat = np.matmul(self.rmat, tmatrix.rmat),
        self.tvec = np.matmul(self.rmat, self.tvec) + tmatrix.tvec

    def inv(self) -> Self:
        return Transformation_Matrix(
            self.rmat.transpose(),
            np.matmul(-self.rmat.transpose(), self.tvec)
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

def plot_FK(L: Tuple[int, int], q: Tuple[int, int], fk: Tuple[int, int]) -> None:
    pass

def GENFK(
    a: np.ndarray, alpha: np.ndarray,
    d: np.ndarray, theta: np.ndarray
) -> Transformation_Matrix:
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