from settings import *


def rotate(angle)->cp.ndarray:
    return cp.array([[cos(angle), -sin(angle), 0],
                     [sin(angle),  cos(angle), 0],
                     [        0,           0 , 1]
                    ], dtype='float32').T
    
def translate(x, y)->cp.ndarray:
    return cp.array([[1, 0, x],
                     [0, 1, y],
                     [0, 0, 1]
                    ], dtype='float32').T

def scale(x, y)->cp.ndarray:
    return cp.array([[x, 0, 0],
                     [0, y, 0],
                     [0, 0, 1]
                    ], dtype='float32').T

def origin_to_center()->cp.ndarray:
    return cp.array([
        [HW, 0, HW],
        [0, HH, HH],
        [0,  0,  0]
    ], dtype='float32').T
