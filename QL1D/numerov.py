import numpy as np
import matplotlib.pyplot as plt
# dpsi/dt = psi(i + 1) - psi(i) / dt
# d^2psi/dt^2 = psi(i + 1) - 2*psi(i) + psi(i - h) / dt^2 (center)

# i hbar dpsi/dt = -hbar^2 /2m d^2 psi / dx^2 + Vpsi
def finite_difference(x, V, m=1, hbar=1):
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
    

if __name__ == "__main__":
    L = 1
N = 300
x = np.linspace(0, L, N)

# potensial (infinite well → 0 di dalam)
V = np.zeros_like(x)

# panggil fungsi kamu
E, psi = finite_difference(x, V, m=1, hbar=1)

dx = x[1] - x[0]

# normalisasi (penting!)
for i in range(3):
    norm = np.sqrt(np.sum(abs(psi[:, i])**2 * dx))
    psi[:, i] /= norm

# energi analitik
n = np.array([1,2,3])
E_analitik = (n**2 * np.pi**2) / 2

# print perbandingan
print("Numerik:", E[:3])
print("Analitik:", E_analitik)

# plot wavefunction
for i in range(3):
    plt.plot(x, psi[:, i], label=f"n={i+1}")

plt.title("Eigenfunction Infinite Square Well")
plt.legend()
plt.show()
