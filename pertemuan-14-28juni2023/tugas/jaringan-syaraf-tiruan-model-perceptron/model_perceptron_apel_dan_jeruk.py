from sklearn.linear_model import Perceptron

# deklarasi input dan target
x = [[1, -1, -1], [-1, 1, 1]]
f_net = [1, -1]

# memanggil fungsi perceptron
perceptron = Perceptron(max_iter=100, tol=0.2, alpha=1, verbose=True)
perceptron.fit(x, f_net)
prediksi = perceptron.predict(x)

# menampilkan hasil prediksi
print("f_net = ", f_net)
print("prediksi dari perceptron = ", prediksi)
