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

    def mul(self, tmat: Self):
        self.rmat = np.matmul(self.rmat, tmat.rmat),
        self.tvec = np.matmul(self.rmat, self.tvec) + tmat.tvec

    def to_np_array(self) -> np.ndarray:
        mat = np.identity(AXES + 1)

        for i in range(AXES):
            for j in range(AXES):
                mat[i][j] = self.rmat[i][j]

        mat[0][AXES] = self.tvec[0]
        mat[1][AXES] = self.tvec[1]
        mat[2][AXES] = self.tvec[2]

        return mat

    # def inv(self) -> Self:
    #     return Transformation_Matrix(
    #         self.rmat.transpose(),
    #         np.matmul(-self.rmat.transpose(), self.tvec)
    #     )

class DH_Transformation_Matrix(Transformation_Matrix):
    def __init__(self) -> None:
        super().__init__()
        self.chain = ""

    def compute_dh(
        self, theta: float, d: float,
        a: float, alpha: float, sigma: bool
    ):
        theta_tmat = Transformation_Matrix()
        theta_tmat.rot(Axis.Z, theta)

        d_tmat = Transformation_Matrix()
        d_tmat.trans(0, 0, d)

        a_tmat = Transformation_Matrix()
        a_tmat.trans(a, 0, 0)

        alpha_tmat = Transformation_Matrix()
        alpha_tmat.rot(Axis.X, alpha)

        self.mul(theta_tmat)
        self.mul(d_tmat)
        self.mul(a_tmat)
        self.mul(alpha_tmat)

        self.chain += "P" if sigma else "R"

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
    d: np.ndarray, theta: np.ndarray,
    sigma: np.ndarray
) -> np.ndarray:
    dh = DH_Transformation_Matrix()

    for thetai, di, ai, alphai, sigmai in zip(
        np.nditer(theta), np.nditer(d),
        np.nditer(a), np.nditer(alpha),
        np.nditer(sigma)
    ):
        dh.compute_dh(thetai, di, ai, alphai, sigmai)

    return dh.to_np_array()

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