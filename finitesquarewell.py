import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# ganti potensial
y = np.linspace(-5, 5, 2000)
psi0 = np.sqrt(2)*np.sin(np.pi*y)
V = np.zeros_like(y)
V[np.abs(y) < 0.2] =- 50

E, psi, norm  = qd.solver.finite_difference(y, V)
g = qd.solver.psi_m2(0.01, E, psi, psi0)


