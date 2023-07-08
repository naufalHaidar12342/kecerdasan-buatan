import numpy as np

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])
y = np.array([0, 0, 0, 1])

w1 = 1

w2 = 1
t = 2
net = (x1 * w1) + (x2 * w2)
y_net = (net >= t).astype(int)
benar = 0
if y_net[0] == y[0]:
    benar += 1
if y_net[1] == y[1]:
    benar += 1
if y_net[2] == y[2]:
    benar += 1
if y_net[3] == y[3]:
    benar += 1

print("Input X1 = ", x1)
print("Input X2 = ", x2)
print("Output Y = ", y)
print()
print("W1 = ", w1)
print("W2 = ", w2)
print("Tetha = ", t)
print()
print("Net = ", net)
print("Y(net) = ", y_net)
print("Bandingkan dengan Y = ", y)
print()
if benar == 4:
    print("Data sudah benar")
else:
    print("Cek Kembali Parameter")
