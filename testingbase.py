import QL1D as qd
import QL1D.util as con
import matplotlib.pyplot as plt
import numpy as np


# gelombang -x^2

# Normalisasi
x = np.linspace(-5, 5, 1000)
psi = np.exp(-x**2)
delta = x[1] - x[0]

# normalisasi
Cpsi, res = qd.alge.normaliza(delta, psi)
print(f"Hasil Faktorisasi Normalisasi : {Cpsi}")
print(f"Hasil Normalisa : {res}")

# probabilitas posisi
posi = qd.alge.posision_x(delta, psi, x)
print(f"Probabilitas Posisi : {posi}")

# momentum 
momen = qd.alge.momentum(delta, psi)
print(f"Probabilitas Momentum : {momen}")

# kinetik energy
kinetic_energy = qd.alge.kinetic_energy(delta, psi, m=1)
print(f"Hasil Probabilitas EK : {kinetic_energy}")

# # ketidakpastian heisenberg
sigma_p = np.sqrt(qd.alge.momentum(delta, psi, pow=2) - momen**2 )
sigma_x = np.sqrt(qd.alge.posision_x(delta, psi, x, pow=2) - posi**2 )

if sigma_p * sigma_x >= con.hbar/2:
    print("Perhitungan Sah")
else:
    print("Perhitungan Tidak Sah")
