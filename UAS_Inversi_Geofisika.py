import numpy as np
import matplotlib.pyplot as plt

# Data Lubang Bor
z = np.array([10, 35, 40, 60, 80])
TC = np.array([41.49, 45.27, 46.05, 48.98, 52])

# Fungsi Misfit
def misfit(m, n):
    errors = TC - (m * z + n)
    return np.sum(errors ** 2)

# Make grid
dm = 0.002
dn = 0.4

# Mengisi Nilai Grid
mi = np.arange(0.1, 0.2 + dm, dm)
ni = np.arange(30, 50 + dn, dn)
mv, nv = np.meshgrid(mi, ni)
tv = np.zeros_like(mv)

for i in range(len(mi)):
    for j in range(len(ni)):
        tv[i, j] = misfit(mi[i], ni[j])

print("misfit pada setiap koordinat : ", tv)
plt.contourf(mv, nv, tv, cmap="gray")
cbar = plt.colorbar()
cbar.set_label(label="Misfit")
plt.xlabel("Gradien Temperatur")
plt.ylabel("Suhu Permukaan")
plt.show()
