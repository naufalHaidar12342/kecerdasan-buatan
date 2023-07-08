import numpy as np

# Definisikan pola masukan
x0 = np.array([-1, -1])
x1 = np.array([-1, 1])
x2 = np.array([-1, -1])
x3 = np.array([1, -1])
x4 = np.array([-1, -1])
x5 = np.array([1, -1])
x6 = np.array([1, -1])
x7 = np.array([-1, -1])
x8 = np.array([1, -1])

# Definisikan pola target
t_pattern = np.array([-1, -1])
u_pattern = np.array([1, -1])

# Inisialisasi matriks bobot
W = np.zeros((2, 2))


# Definisikan fungsi aktivasi
def aktivasi(x):
    return 1 if x >= 0 else -1


# Jalankan algoritma pembelajaran Hebb
for x in [x0, x1, x2, x3, x4, x5, x6, x7, x8]:
    X = np.reshape(x, (2, 1))
    W += np.dot(X, X.T)

# Uji matriks bobot yang telah dipelajari
test_patterns = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
patterns_recognized = []
for pattern in test_patterns:
    y = np.dot(W, pattern)
    output = np.array([aktivasi(val) for val in y])
    if np.array_equal(output, t_pattern) and "Pola T" not in patterns_recognized:
        patterns_recognized.append("Pola T")
    elif np.array_equal(output, u_pattern) and "Pola U" not in patterns_recognized:
        patterns_recognized.append("Pola U")

# Cetak hasil pengenalan pola
for pattern in patterns_recognized:
    print(pattern, "dikenali.")

# uji pola rusak
x0 = np.array([-1, -1])
x1 = np.array([1, 1])
x2 = np.array([1, -1])
x3 = np.array([-1, 1])
x4 = np.array([1, 1])
x5 = np.array([-1, -1])
x6 = np.array([1, 1])
x7 = np.array([-1, 1])
x8 = np.array([1, -1])
