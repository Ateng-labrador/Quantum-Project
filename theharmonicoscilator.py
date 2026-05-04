import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con

# The Harmonic Oscillator
y = np.linspace(-5, 5, 2000)
K = 0.02
omega = 0.3
V = (1/2)*1*omega * y**2

E, psi = qd.solver.finite_difference(y, V)



# plt.bar(np.arange(0, 10, 1), E[0:10])

# plt.plot(y, V)
plt.show()
