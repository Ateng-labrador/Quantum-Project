import numpy as np
from grid.Grid import Grid as grid

class WaveFunction:
    def __init__(self, grid):
        self.grid = grid
        self.psi = np.zeros_like(grid.x, dtype = complex)
    
    def normaliza(self):
        dx = self.grid.dx
        norm = np.sum(np.abs(self.psi)**2) * dx
        self.psi /= norm
