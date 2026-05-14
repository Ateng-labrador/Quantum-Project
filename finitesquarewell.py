import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# finite square
y = np.linspace(0, 1, 200)
psi0 = np.sin(np.pi*y)
V = np.zeros_like(y)
V[np.abs(y) < 0.2] =- 50

E, psi, norm  = qd.solver.finite_difference(y, V)
g = qd.solver.psi_m2(0.01, E, psi, psi0)

