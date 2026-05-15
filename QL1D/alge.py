import numpy as np

def normaliza(delta, psi):
    """Normalisasi fungsi gelombang.

    Parameters
    ----------
    delta : float
        Spasi grid.
    psi : array_like
        Nilai fungsi gelombang.

    Returns
    -------
    psi : ndarray
        Fungsi gelombang yang telah dinormalisasi.
    res : float
        Nilai pengecekan normalisasi (jumlah |psi|^2 * delta).

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(-5, 5, 100)
    >>> delta = x[1] - x[0]
    >>> psi = np.exp(-(x**2) / 2)  # Fungsi Gaussian
    >>> psi_norm, res = normaliza(delta, psi)
    >>> ress
    1.0000000000015827
    """
    area = 0
    for i in range(1, len(psi)-1):
        area += abs(psi[i])**2 *delta
    
    # mencari faktor normalisasi
    for i in range(len(psi)):
        psi[i] = psi[i]/area**0.5
    
    # check
    res = np.sum(abs(psi)**2 * delta)

    return psi ,res


def posision_x(delta, psi, x, pow = 1):
    """Hitung nilai ekspektasi posisi.

    Parameters
    ----------
    delta : float
        Spasi grid.
    psi : array_like
        Nilai fungsi gelombang.
    x : array_like
        Grid posisi.
    pow : int, optional
        Pangkat nilai ekspektasi. ``1`` untuk <x>, ``2`` untuk <x^2>.

    Returns
    -------
    res : float
        Nilai ekspektasi posisi atau momen kedua.

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(-5, 5, 100)
    >>> delta = x[1] - x[0]
    >>> psi = np.exp(-(x**2) / 2) / (np.pi**0.25)  # Gaussian ternormalisasi
    >>> posisi_mean = posision_x(delta, psi, x, pow=1)
    >>> posisi_var = posision_x(delta, psi, x, pow=2)
    <x> = 0.000000, <x^2> = 0.500000
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
    """Hitung nilai ekspektasi momentum atau momen operator momentum.

    Parameters
    ----------
    delta : float
        Spasi grid.
    psi : array_like
        Nilai fungsi gelombang.
    hbar : float, optional
        Konstanta Planck tereduksi. Default adalah 1.
    pow : int, optional
        Pangkat operator: ``1`` untuk nilai ekspektasi momentum, ``2`` untuk operator turunan kedua.

    Returns
    -------
    res : complex
        Nilai ekspektasi momentum atau momen terkait momentum.

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(-5, 5, 100)
    >>> delta = x[1] - x[0]
    >>> psi = np.exp(-(x**2) / 2)  # Fungsi Gaussian
    >>> p_exp = momentum(delta, psi, hbar=1, pow=1)
    >>> p2_exp = momentum(delta, psi, hbar=1, pow=2)
    >>> p_exp
    >>> -1.3970501884714543e-17j 
    >>> p_2_exp
    >>> (0.8850976098180809+0j)
    
    """
    if pow == 1:
        res = 0 + 0j
        for i in range(1, len(psi) - 1):
            dpsi_dx = (psi[i+1] - psi[i-1]) / (2*delta)
            res += np.conj(psi[i]) * (-1j * hbar * dpsi_dx) * delta
        return res
    elif pow == 2:
        res = 0 + 0j
        for i in range(1, len(psi) - 1):
            d2psi_dx2 = (psi[i + 1] - 2*psi[i] + psi[i - 1])/delta**2
            res += np.conj(psi[i]) * (-hbar**2 * d2psi_dx2) * delta
        return res
    else:
        return "error"


def energi_kinetik(delta, psi, m = 1, hbar=1):
    """Hitung nilai ekspektasi energi kinetik.

    Parameters
    ----------
    delta : float
        Spasi grid.
    psi : array_like
        Nilai fungsi gelombang.
    m : float
        Massa partikel.
    hbar : float, optional
        Konstanta Planck tereduksi. Default adalah 1.

    Returns
    -------
    res : complex
        Nilai ekspektasi energi kinetik.

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(-5, 5, 100)
    >>> delta = x[1] - x[0]
    >>> psi = np.exp(-(x**2) / 2)  # Fungsi Gaussian
    >>> E_k = energi_kinetik(delta, psi, m=1, hbar=1)
    >>> E_k
    >>> (0.44254880490904047-0j)
    """
    res = 0 + 0j
    for i in range(1, len(psi) - 1):
        d2psi_dx = (psi[i + 1] - 2*psi[i] + psi[i - 1]) / delta**2
        res += np.conj(psi[i]) * d2psi_dx * delta
    return (-hbar**2 / 2*m) * res
