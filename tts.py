import QL1D as qd
import numpy as np


x = np.linspace(0, 1, 100)
V = 0.5 * x**2  # Potensial harmonik
E, psi, norm_check = qd.solver.finite_difference(x, V, m=1, hbar=1)
print(f"Eigenenergi (5 tingkat terendah): {E[:5]}")
print(f"Normalisasi: {norm_check}")
