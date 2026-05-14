import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# infiniteSquareWell
y = np.linspace(0, 1, 200)
V = np.zeros_like(y)
psi0 = np.sqrt(2)*np.sin(np.pi*y)
x1 = np.array([1, 2, 3])
E_analitik = (x1**2 * np.pi**2)/2

E, psi, norm = qd.solver.finite_difference(y, V)

g = qd.solver.psi_m2(0.01, E, psi, psi0)


