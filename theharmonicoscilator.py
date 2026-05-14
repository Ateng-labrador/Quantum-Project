import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# The Harmonic Oscillator
y = np.linspace(0, 1, 200)
V = (1/2)* y**2

E, psi, norm = qd.solver.finite_difference(y, V)
x = np.array([1, 2, 3, 4, 5])
E_analitik = x + 0.5

print(E[:5])
print(E_analitik)


