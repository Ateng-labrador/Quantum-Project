import QL1D as qd
import QL1D.util as con
import numpy as np
import matplotlib.pyplot as plt

# Potensial gaussian
x = np.linspace(0, 1, 2000)
V = 1000*np.exp(-(x - 0.4)**2 / (2*0.05**2))
# plt.plot(x, V)

#mencari potensial
E, psi = qd.solver.finite_difference(x, V)


# mencari energi
plt.bar(np.arange(0, 10, 1), E[0:10])

plt.show()

