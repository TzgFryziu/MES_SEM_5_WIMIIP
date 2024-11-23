import numpy as np


class Jacobian:
    def __init__(self, j):
        self.J = j
        self.J1 = np.linalg.inv(self.J)
        self.detJ = np.linalg.det(self.J)
