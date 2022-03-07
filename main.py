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
    # Make assertions more robust!
    assert len(L) == 2, f"Expected 2 by 1 Vector, found {len(L)} by 1 Vector"
    assert len(q) == 2, f"Expected 2 by 1 Vector, found {len(q)} by 1 Vector"

    # Forward kinematics units
    # * Translation vectors
    # * Rotation matrices

    P = []

    return P

if __name__ == '__main__':
    # TODO
    pass