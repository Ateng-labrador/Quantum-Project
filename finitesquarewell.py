import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# ganti potensial
y = np.linspace(-5, 5, 2000)
psi0 = np.sqrt(2)*np.sin(np.pi*y)
V = np.zeros_like(y)
V[np.abs(y) < 0.2] =- 50
# plt.plot(y, V)
# plt.show()

E, psi, norm  = qd.solver.finite_difference(y, V)
g = qd.solver.psi_m2(0.01, E, psi, psi0)
# print(norm)

# plt.plot(psi.T[0]**2)
# plt.plot(psi.T[1]**2)
# plt.plot(psi.T[2]**2)
# plt.plot(psi.T[3]**2)
# plt.plot(y, g)
plt.bar(np.arange(0, 200, 1), E[0:200])
plt.show()

