import math

from typing import List

Vector = List[float]

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