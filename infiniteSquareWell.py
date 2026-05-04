import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con


# infiniteSquareWell
y = np.linspace(-5, 5, 2000)
V = np.zeros_like(y)

E, psi = qd.solver.finite_difference(y, V)
plt.plot(psi.T[0]**2)
plt.plot(psi.T[1]**2)
plt.plot(psi.T[2]**2)
plt.plot(psi.T[3]**2)

# plt.bar(np.arange(0, 10, 1), E[0:10])
plt.show()
