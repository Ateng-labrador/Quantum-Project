import numpy as np

class Grid:
    def __init__(self, x_min, x_max, N):
        self.x = np.linspace(x_min, x_max, N)
        self.dx = self.x[1] - self.x[0]

if __name__ == "__main__":
    test = Grid(12, 100, 1000)
    print(test.x)
