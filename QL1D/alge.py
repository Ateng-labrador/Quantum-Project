import numpy as np
import util as constat

def normaliza(delta, psi):
    """
    Fungsi Untuk Melakukan Normalisasi Fungsi

    return:
    psi = faktor normalisasi
    res = hasil normalisasi
    """
    area = 0
    for i in range(1, len(psi)-1):
        area = area + abs(psi[i])**2 *delta
    
    # mencari faktor normalisasi
    for i in range(len(psi)):
        psi[i] = psi[i]/area**0.5
    
    # check
    res = np.sum(abs(psi)**2 * delta)

    return psi ,res


def posision_x(delta, psi, x, pow = 1):
    """
    Fungsi Untuk Mencari Probabilitas Posisi Suatu Fungsi

    return:
    res = hasil kalkulasi persamaan posisi
    """
    if pow == 1:
        res = np.sum(x * abs(psi)**2 * delta)
        return res
    elif pow == 2:
        res = np.sum(x**2 * abs(psi)**2 * delta)
        return res
    else:
        return "Error"


def momentum(delta, psi, hbar = 1, pow = 1):
    """
    Fungsi Untuk menentukan probabilitas momentum
    
    return:
    res : hasil kalkulasi persamaan
    """
    if pow == 1:
        res = 0 + 0j
        for i in range(1, len(psi) - 1):
            dpsi_dx = (psi[i+1] - psi[i-1]) / (2*delta)
            res += np.conj(psi[i] * (-1j * hbar * dpsi_dx)) * delta
        return res
    elif pow == 2:
        res = 0 + 0j
        for i in range(1, len(psi) - 1):
            d2psi_dx2 = (psi[i + 1] - 2*psi[i] + psi[i - 1])/delta**2
            res += np.conj(psi[i] * (-hbar**2 * d2psi_dx2)**2) * delta
        return res
    else:
        return "error"
    

def kinetic_energy(delta, psi, m,hbar=1):
    """
    Fungsi untuk menghitung energi kinetik dari fungsi gelombang


    return:
    res : hasil kalkulasi energi kinetik
    """
    res = 0 + 0j
    for i in range(1, len(psi) - 1):
        d2psi_dx = (psi[i + 1] - 2*psi[i] + psi[i - 1]) / delta**2
        res += np.conj(psi[i]) * d2psi_dx * delta
    return (-hbar**2 / 2*m) * res


if __name__ == "__main__":
    x = np.linspace(-5, 5, 1000)
    psi = np.exp(-x**2)
    delta = x[1] - x[0]
    psi, res = normaliza(delta, psi)
    # hasil = posision_x(delta, psi, x)
    # momen = momentum(delta, psi)
    # kinetik = kinetic_energy(delta, psi, 2)
    sigma_x = np.sqrt(posision_x(delta, psi, x, pow=2) - posision_x(delta, psi, x)**2)
    sigma_p = np.sqrt(momentum(delta, psi, pow=2) - momentum(delta, psi)**2)
    if sigma_p*sigma_x >= constat.hbar/2:
        print("Sah")
    else:
        print("tdk sah")
