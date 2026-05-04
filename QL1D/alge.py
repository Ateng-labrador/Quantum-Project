import numpy as np

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
