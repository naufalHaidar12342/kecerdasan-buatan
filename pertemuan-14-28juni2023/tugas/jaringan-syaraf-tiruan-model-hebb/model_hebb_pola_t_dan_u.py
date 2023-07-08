import numpy as np

# deklarasi pola T
pola_t = np.array([-1, -1, -1, 1, -1, 1, 1, -1, 1])
pola_u = np.array([-1, 1, -1, -1, 1, -1, -1, -1, -1])

# deklarasi target
target_pola_t = 1
target_pola_u = -1

# menghitung delta weight untuk pola T
t_delta_w = target_pola_t * pola_t
print("deltaW pola T = ", t_delta_w)

# menghitung delta bias untuk pola T
t_delta_bias = target_pola_t

# menghitung delta weight untuk pola U
u_delta_w = target_pola_u * pola_u
print("deltaW pola U = ", u_delta_w)

# menghitung delta bias untuk pola U
u_delta_bias = target_pola_u

# deklarasi bobot inisiasi dan bias inisiasi
w_inisiasi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
bias_inisiasi = 0

# menghitung bobot baru untuk pola T dan U
t_weight_baru = w_inisiasi + t_delta_w
print("Wbaru pola T = ", t_weight_baru)
u_weight_baru = w_inisiasi + u_delta_w
print("Wbaru pola U = ", u_weight_baru)

# menghitung net
t_net = np.dot(t_weight_baru, pola_t) + t_delta_bias
print("net dari pola T = ", t_net)
u_net = np.dot(u_weight_baru, pola_u) + u_delta_bias
print("net dari pola U = ", u_net)

# menghitung f(net)/hasil fungsi aktivasi
t_f_net = 0
if t_net >= 0:
    t_f_net = 1
else:
    t_f_net = -1
print("f(net) pola T = ", t_f_net)

u_f_net = 0
if u_net >= 0:
    u_f_net = 1
else:
    u_f_net = -1
print("f(net) pola U = ", u_f_net)

# penarikan kesimpulan
hasil_pola_t = ""
if t_f_net == target_pola_t:
    hasil_pola_t = "Pola T dikenali model Hebb"
else:
    hasil_pola_t = "Pola T tidak dikenali model Hebb"

hasil_pola_u = ""
if u_f_net == target_pola_u:
    hasil_pola_u = "Pola U dikenali model Hebb"
else:
    hasil_pola_u = "Pola U tidak dikenali model Hebb"

print("pola T dengan model Hebb= ", hasil_pola_t)
print("pola U dengan model Hebb= ", hasil_pola_u)
