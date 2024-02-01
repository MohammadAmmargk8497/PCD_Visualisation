from scipy.spatial.transform import Rotation as R
import numpy as np
import numpy.matlib as matlib
from math import sin, cos, atan2, sqrt


MATRIX_MATCH_TOLERANCE = 1e-4


def build_se3_transform(xyzrpy):
    """Creates an SE3 transform from translation and Euler angles.
    Args:
        xyzrpy (list[float]): translation and Euler angles for transform. Must have six components.
    Returns:
        numpy.matrixlib.defmatrix.matrix: SE3 homogeneous transformation matrix
    Raises:
        ValueError: if `len(xyzrpy) != 6`
    """
    if len(xyzrpy) != 6:
        raise ValueError("Must supply 6 values to build transform")

    se3 = matlib.identity(4)
    se3[0:3, 0:3] = euler_to_so3(xyzrpy[3:6])
    se3[0:3, 3] = np.matrix(xyzrpy[0:3]).transpose()
    return np.array(se3)

def euler_to_so3(rpy):
    """Converts Euler angles to an SO3 rotation matrix.
    Args:
        rpy (list[float]): Euler angles (in radians). Must have three components.
    Returns:
        numpy.matrixlib.defmatrix.matrix: 3x3 SO3 rotation matrix
    Raises:
        ValueError: if `len(rpy) != 3`.
    """
    if len(rpy) != 3:
        raise ValueError("Euler angles must have three components")

    R_x = np.matrix([[1, 0, 0],
                     [0, cos(rpy[0]), -sin(rpy[0])],
                     [0, sin(rpy[0]), cos(rpy[0])]])
    R_y = np.matrix([[cos(rpy[1]), 0, sin(rpy[1])],
                     [0, 1, 0],
                     [-sin(rpy[1]), 0, cos(rpy[1])]])
    R_z = np.matrix([[cos(rpy[2]), -sin(rpy[2]), 0],
                     [sin(rpy[2]), cos(rpy[2]), 0],
                     [0, 0, 1]])
    R_zyx = R_z * R_y * R_x
    return R_zyx