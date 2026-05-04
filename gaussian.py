import QL1D as qd
import QL1D.util as con
import numpy as np
import matplotlib.pyplot as plt

# Potensial gaussian
x = np.linspace(0, 1, 301)
V = -1e-2*np.exp(-(x-1/2)**2/(2*(1/20)**2))
psi0 = np.sqrt(2)*np.sin(np.pi*x)
# plt.plot(x, V)

#mencari potensial
E, psi = qd.solver.finite_difference(x, V)

#plot state
plt.plot(psi.T[0]**2)
plt.plot(psi.T[1]**2)
plt.plot(psi.T[2]**2)
plt.plot(psi.T[3]**2)

# plot energi
# plt.bar(np.arange(0, 200, 1), E[0:200])

# mencari solusi TDSE
# E_js = E
# cs = np.dot(psi.T, psi0)
# def psi_m2(t):
#     return psi@(cs*np.exp(-1j*E_js*t))

# g = np.abs(psi_m2(0.01))**2

# plt.plot(x, psi0**2)
# plt.plot(x, g)
plt.show()
