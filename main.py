import math

from typing import List
from typing import Tuple
from typing_extensions import Self

Vector = List[float]

class Translation_Vector:
    pass

class Matrix:
    def __init__(self, rows: int, cols: int):
        self._ROWS = rows
        self._COLS = cols
        self._values = [0.] * self._ROWS * self._COLS

    def _get_index(self, coordinate: Tuple[int, int]) -> int:
        return self._COLS * coordinate[0] + coordinate[1]

    def multiplication(self, matrix: Self) -> Self:
        # TODO
        # * Implement Strassen algorithm

        assert self._ROWS == matrix._COLS

        mult = Matrix(matrix._ROWS, self._COLS)

        # Really slow!
        for i in range(self._COLS):
            for j in range(matrix._ROWS):
                for k in range(self._ROWS):
                    pass

        return mult

    def from_list(self, l: List[float]):
        pass

    def at(self, coordinate: Tuple[int, int]) -> float:
        return self._values[self._get_index(coordinate)]
class Rotation_Matrix:
    pass

class Transformation_Matrix:
    pass

def FK(L: Vector, q: Vector) -> Vector:
    """
    Solves the forward kinematics of a planar 2R robot.

    Returns:
        @P (Vector): 2 by 1 vector containing the end effector's x and y 
            coordinates expressed in the base frame.
    """
    # TODO
    # Make assertions more robust!
    # Test function against several cases, including edge cases.

    assert len(L) == 2, f"Expected 2 by 1 Vector, found {len(L)} by 1 Vector"
    assert len(q) == 2, f"Expected 2 by 1 Vector, found {len(q)} by 1 Vector"

    # Forward kinematics units
    # * Translation vectors
    # * Rotation matrices

    angle_sum: float = sum(q)

    L1 = L[0]
    L2 = L[1]

    P = [
        math.cos(angle_sum), -math.sin(angle_sum), 0, L1 * math.cos(angle_sum) + L1 * math.cos(q[0]),
        math.sin(angle_sum), math.cos(angle_sum), 0, L2 * math.sin(angle_sum) + L2 * math.sin(q[0]),
        0, 0, 1, 0,
        0, 0, 0, 1
    ]

    return P

if __name__ == '__main__':
    # TODO
    pass