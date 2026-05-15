import numpy as np

def finite_difference(x, V, m=1, hbar=1):
    """Selesaikan persamaan Schrödinger dengan metode beda hingga.

    Parameters
    ----------
    x : array_like
        Grid posisi.
    V : array_like
        Potensial pada setiap titik grid.
    m : float, optional
        Massa partikel. Default adalah 1.
    hbar : float, optional
        Konstanta Planck tereduksi. Default adalah 1.

    Returns
    -------
    E : ndarray
        Nilai eigenenergi.
    psi_full : ndarray
        Fungsi gelombang lengkap untuk setiap mode eigen.
    res : float
        Hasil pengecekan normalisasi (jumlah |psi|^2 * deltax).

    Examples
    --------
    >>> import numpy as np
    >>> x = np.linspace(0, 1, 100)
    >>> V = 0.5 * x**2  # Potensial harmonik
    >>> E, psi, norm_check = finite_difference(x, V, m=1, hbar=1)
    >>> E[:5]
    [5.07516768  19.89307139  44.54363807  79.01602487 123.27714695]
    >>> norm_check
    0.9898989898989901
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

    # check normalize
    res = np.sum(abs(psi_full)**2 * deltax)

    return E, psi_full, res

def psi_m2(t, E, psi, psi0):
    """Hitung densitas probabilitas dari evolusi waktu gelombang.

    Parameters
    ----------
    t : float or ndarray
        Waktu evolusi.
    E : array_like
        Eigenenergi.
    psi : ndarray
        Eigenstat.
    psi0 : ndarray
        Kondisi awal fungsi gelombang.

    Returns
    -------
    result : ndarray
        Densitas probabilitas |psi(t)|^2 setelah evolusi waktu.

    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> x = np.linspace(0, 1, 301)
    >>> -1e-2*np.exp(-(x-1/2)**2/(2*(1/20)**2))
    >>> psi0 = np.sqrt(2)*np.sin(np.pi*x)
    >>> E, psi, norm = finite_difference(x, V)
    >>> g = psi_m2(0.01, E, psi, psi0)
    >>> plt.plot(x, g)
    """
    E_js = E
    cs = np.dot(psi.T, psi0)
    sigma = psi@(cs*np.exp(-1j*E_js*t))
    return np.abs(sigma)**2
