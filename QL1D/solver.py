import numpy as np
import matplotlib.pyplot as plt


def finite_difference(x, V, m=1, hbar=1):
    """
    Menyelesaikan persamaan shroodinger dengan metode
    finite difference

    return:
    E : Eigenvalue
    psi : Eigenvector
    """
    deltax = x[1] - x[0]
    diag = []
    off = -(hbar**2)/(2 * m * deltax**2)
    for i in range(1, len(x) - 1):
        koe = (hbar**2)/(m * deltax**2) + V[i]
        diag.append(koe)
    
    # make matriks tridiagona
    H = np.zeros((len(x) - 2, len(x) - 2))
    for i in range(len(x) - 2):
        H[i, i] = diag[i]
        if i > 0:
            H[i, i - 1] = off
        if i < len(x) - 3:
            H[i, i + 1] = off 

    E, psi = np.linalg.eigh(H)

    psi_full = np.zeros((len(x), psi.shape[1]))
    for j in range(psi.shape[1]):
        for i in range(1, len(x) - 1):
            psi_full[i, j] = psi[i - 1, j]

    return E, psi_full


# if __name__ == "__main__":
#     # E psi = H psi
#     # psi = itu eigen vector
#     # H = adalah eigen value
#     N = 2000
#     y = np.linspace(0, 1, N+1)
    
#     V = 1000*np.exp(-(y-0.7)**2 / (2*0.05**2))
#     # plt.plot(y, V)
#     E, psi = finite_difference(y, V)
#     plt.bar(np.arange(0, 10, 1), E[0:10])
#     plt.show()
