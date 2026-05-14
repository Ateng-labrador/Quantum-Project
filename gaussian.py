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

# plt.plot(x ,psi.T[0]**2)
# plt.plot(x ,psi.T[1]**2)
# plt.plot(x ,psi.T[2]**2)
# plt.plot(x ,psi.T[3]**2)
# plt.title(r'$|\Psi|^2$')
# plt.ylabel(r'$\Psi_{n}$')
# plt.xlabel(r'$x$')

# plt.title("Energi dari gelombang")
# plt.xlabel("Posisi")
# plt.ylabel("Energi")
# plt.bar([i for i in range(0, 10, 1)], E[0:10])

# t = 0.01
# g = qd.solver.psi_m2(t, E, psi, psi0)
# plt.title(r'Probabilitas $|\Psi(x,t)|^2$')
# plt.xlabel(r'$x$')
# plt.ylabel(r'$|\Psi(x,t)|^2$')
# plt.plot(x, abs(g)**2)
# plt.grid()
# plt.show()

# plt.title(r'Gaussian Potential $V(x) = -0.01 \exp\left( -\frac{(x - 0.5)^2}{2 \cdot (0.05)^2} \right)$')
# plt.grid()
# plt.show()
