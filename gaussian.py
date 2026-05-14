import QL1D as qd
import QL1D.util as con
import numpy as np
import matplotlib.pyplot as plt

# Potensial gaussian
x = np.linspace(0, 1, 301)
V = -1e-2*np.exp(-(x-1/2)**2/(2*(1/20)**2))
psi0 = np.sqrt(2)*np.sin(np.pi*x)

#mencari potensial
E, psi, norm = qd.solver.finite_difference(x, V)
