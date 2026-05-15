# Potensial Harmonik

Potensial harmonik kuantum (quantum harmonic oscillator) merupakan salah satu model paling penting dalam mekanika kuantum karena banyak sistem fisika nyata dapat didekati sebagai osilator harmonik di sekitar titik kesetimbangannya. Model ini digunakan untuk mendeskripsikan getaran molekul, fonon pada kristal, hingga pendekatan medan kuantum.

Pada osilator harmonik, potensial berubah secara kuadratik terhadap posisi sehingga partikel mengalami gaya pemulih yang sebanding dengan perpindahannya. Potensial didefinisikan sebagai:

$$
V(x) = \frac{1}{2}  y^2
$$

Tingkat energi sistem bersifat terkuantisasi dan diberikan oleh:

$$
E = (\frac{1}{2} + n)
$$

dengan:

$n = 1, 2, 3, 4, ...., i$
Menariknya, bahkan pada keadaan dasar (n=0), sistem masih memiliki energi minimum yang disebut zero-point energy.

Pada contoh ini fungsi gelombang awal diberikan sebagai:

$$
\Psi_0 = exp^{-y^2}
$$

yang memiliki bentuk Gaussian dan umum digunakan sebagai pendekatan keadaan dasar osilator harmonik kuantum.

**Setup Invorment**
```
import numpy as np
import matplotlib.pyplot as plt
import QL1D as qd
import QL1D.util as con
```

**Parameter**
```
y = np.linspace(0, 1, 200)
V = (1/2)* y**2
```


**Menyelesaikan Persamaan Shroodinger TISE**

```
E, psi, norm = qd.solver.finite_difference(y, V)
```

**Grafik Probabilitas TISE**
```
plt.title("Grafik Probabilitas TISE")
plt.plot(y, psi.T[0]**2)
plt.plot(y, psi.T[1]**2)
plt.plot(y, psi.T[2]**2)
plt.plot(y, psi.T[3]**2)
plt.xlabel("Posisi")
plt.ylabel(r'$|\Psi(x)|^2$')
plt.grid()
plt.show()
```
![Potensial Harmonik](assets/harmonik/Probabilitas%20TISE.png)


**Grafik Probabilitas TDSE**
```

plt.title("Grafik Probabilitas TDSE")
plt.plot(y, abs(g)**2)
plt.xlabel("Posisi")
plt.ylabel(r'$|\Psi(x,t)|^2$')
plt.grid()
plt.show()
```
![Potensial Harmonik](assets/harmonik/Probabilitas%20TDSE.png)

**Perbandingan hasil analitik dan numerik**
```
x = np.array([i for i in range(1, 10, 1)])
E_analitik = x + 0.5
```

```
E[:5]
```

```
[1.49960533 2.49897379 3.49802729 4.4967749  5.49528041]
```

```
E_analitik
```

```
[1.5 2.5 3.5 4.5 5.5]
```

**Grafik Energi Analitik Dan Numerik**
```
plt.title("Grafik Perbandingan Energi")
plt.bar([i for i in range(1, 10, 1)], E[1:10], label='Numerik')
plt.plot(x, E_analitik, 'ro--',label='Analitik')
plt.xlabel("Posisi")
plt.ylabel("Energi")
plt.legend()
plt.grid()
plt.show()
```

![Potensial Harmonik](assets/harmonik/Grafik%20Energi%20Harmonik.png)
