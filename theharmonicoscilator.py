import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con




# The Harmonic Oscillator
y = np.linspace(-5, 5, 2000)
V = (1/2)* y**2

E, psi, norm = qd.solver.finite_difference(y, V)
x = np.arange(5)
E_analitik = x + 0.5
# g = qd.solver.psi_m2(0.01, E, psi, psi0)
print(E[:5])
print(E_analitik)

# plt.bar(np.arange(0, 10, 1), E[0:10])

# plt.plot(y, V)
# plt.show()
