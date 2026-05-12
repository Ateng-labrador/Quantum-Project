# Solver
Modul `QL1D.solver` menyediakan metode numerik yang digunakan untuk menyelesaikan Persamaan Schrödinger satu dimensi. Modul ini berisi berbagai algoritma inti untuk menghitung fungsi gelombang, energi eigen, serta evolusi sistem kuantum secara numerik.

Fungsi-fungsi dalam modul ini dirancang untuk bekerja secara efisien pada simulasi TISE maupun TDSE dengan memanfaatkan pendekatan numerik berbasis grid. Implementasi solver difokuskan pada kemudahan penggunaan, stabilitas perhitungan, dan fleksibilitas dalam menangani berbagai bentuk potensial kuantum.


***QL1D.solver.finite_difference***

`solver.finite_difference(x, V, m=1, hbar=1)`

::: QL1D.solver.finite_difference

***QL1D.solver.psi_m2***

`solver.psi_m2(t, E, psi, psi0)`

::: QL1D.solver.psi_m2