import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# infiniteSquareWell
y = np.linspace(0, 1, 2000)
V = np.zeros_like(y)
psi0 = np.sqrt(2)*np.sin(np.pi*y)
x1 = np.array([1, 2, 3])
E_analitik = (x1**2 * np.pi**2)/2

E, psi, res = qd.solver.finite_difference(y, V)
# g = qd.solver.psi_m2(0.01, E, psi, psi0)
# plt.plot(psi.T[0])
# plt.plot(psi.T[1])
# plt.plot(psi.T[2]**2)
# plt.plot(psi.T[3]**2)
# plt.plot(y, psi[:, 0], label="n=1")
# plt.plot(y, psi[:, 1], label="n=1")


# plt.bar(np.arange(0, 10, 1), E[0:10])
# plt.plot(y, g)
print(E[:3])
print(E_analitik[:3])
# plt.show()
