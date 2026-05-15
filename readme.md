![banner](.github/QL1D.png)

QL1D adalah library open-source yang dirancang untuk menyelesaikan persamaan Schrödinger satu dimensi (1D) secara numerik. Library ini memanfaatkan array dari NumPy untuk merepresentasikan operator dan fungsi gelombang, sehingga memungkinkan komputasi yang efisien dan performa yang optimal dalam proses perhitungan eigenvalue dan eigenstate.

```python
import QL1D as qd
import numpy as np

x = np.linspace(1, 5, 2000)
delta = x[1] - x[0]
psi = np.exp(-(x**2)/2)
faktor_norm, res = qd.alge.normaliza(delta, psi)
print(f'Hasil faktor Normalisasi :{faktor_norm}')
print(f'Hasil Normalisasi :{res}')
```

## Requirements

Untuk menjalankan Library ini, di perlukan Memiliki Python versi: 3.14.3

## Instalasi

Silahkan install package `QL1D` via pip

```bash
pip install QL1D==0.2.0
```

Informasi:

Silahkan melihat [Wiki](https://ateng-labrador.github.io/Quantum-Project/) untuk dokumentasi dan contoh penggunaannya
