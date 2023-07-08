import numpy as np

# uji coba dengan model rusak
pola_rusak_1 = np.array([-1, 1, 1, -1, 1, -1, 1, -1, 1])
pola_rusak_2 = np.array([-1, 1, -1, 1, 1, -1, 1, 1, -1])

target_pola_t = 1
target_pola_u = -1

w_inisiasi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
bias_inisiasi = 0

# menghitung delta bias untuk pola T
t_delta_bias = target_pola_t
# menghitung delta bias untuk pola U
u_delta_bias = target_pola_u

# menghitung delta W untuk pola rusak 1 dan 2
# dengan target pola yang dituju: pola T
rusak_1_delta_w = target_pola_t * pola_rusak_1
print("targetnya pola T,deltaW pola rusak 1= ", rusak_1_delta_w)
rusak_2_delta_w = target_pola_t * pola_rusak_2
print("targetnya pola T,deltaW pola rusak 2= ", rusak_2_delta_w)

# menghitung W baru untuk pola rusak 1 dan 2
# target pola yang dituju: pola T
rusak_1_weight_baru = w_inisiasi + rusak_1_delta_w
print("targetnya pola T,W baru pola rusak 1= ", rusak_1_weight_baru)
rusak_2_weight_baru = w_inisiasi + rusak_2_delta_w
print("targetnya pola T,W baru pola rusak 2= ", rusak_2_weight_baru)

# menghitung net untuk pola rusak 1 dan 2
# target pola yang dituju: pola T
rusak_1_net = np.dot(rusak_1_weight_baru, pola_rusak_1) + t_delta_bias
print("targetnya pola T,net pola rusak 1= ", rusak_1_net)
rusak_2_net = np.dot(rusak_2_weight_baru, pola_rusak_2) + t_delta_bias
print("targetnya pola T,net pola rusak 2= ", rusak_2_net)

# menghitung f(net) untuk pola rusak 1 dan 2
# target pola yang dituju: pola T
rusak_1_f_net = 0
if rusak_1_net >= 0:
    rusak_1_f_net = 1
else:
    rusak_1_f_net = -1
print("targetnya pola T,f(net) pola rusak 1= ", rusak_1_f_net)

rusak_2_f_net = 0
if rusak_2_net >= 0:
    rusak_2_f_net = 1
else:
    rusak_2_f_net = -1
print("targetnya pola T,f(net) pola rusak 2= ", rusak_2_f_net)

# penarikan kesimpulan
hasil_rusak_1 = ""
if rusak_1_f_net == target_pola_t:
    hasil_rusak_1 = "Pola rusak 1 dikenali model Hebb sebagai pola T"
else:
    hasil_rusak_1 = "Pola rusak 1 tidak dikenali model Hebb sebagai pola T"
print("targetnya pola T,hasil pengenalan pola rusak 1= ", hasil_rusak_1)

hasil_rusak_2 = ""
if rusak_2_f_net == target_pola_t:
    hasil_rusak_2 = "Pola rusak 2 dikenali model Hebb sebagai pola T"
else:
    hasil_rusak_2 = "Pola rusak 2 tidak dikenali model Hebb sebagai pola T"
print("targetnya pola T,hasil pengenalan pola rusak 2= ", hasil_rusak_2)

"""  """

"""uji coba dengan model rusak, targetnya dibalik
pola rusak 1 targetnya pola U, pola rusak 2 targetnya pola U """

# menghitung delta W untuk pola rusak 1 dan 2
# dengan target pola yang dituju: pola U
rusak_1_delta_w = target_pola_u * pola_rusak_1
print("targetnya pola U,deltaW pola rusak 1= ", rusak_1_delta_w)
rusak_2_delta_w = target_pola_u * pola_rusak_2
print("targetnya pola U,deltaW pola rusak 2= ", rusak_2_delta_w)

# menghitung W baru untuk pola rusak 1 dan 2
# target pola yang dituju: pola U
rusak_1_weight_baru = w_inisiasi + rusak_1_delta_w
print("targetnya pola U,W baru pola rusak 1= ", rusak_1_weight_baru)
rusak_2_weight_baru = w_inisiasi + rusak_2_delta_w
print("targetnya pola U,W baru pola rusak 2= ", rusak_2_weight_baru)

# menghitung net untuk pola rusak 1 dan 2
# target pola yang dituju: pola U
rusak_1_net = np.dot(rusak_1_weight_baru, pola_rusak_1) + u_delta_bias
print("targetnya pola U,net pola rusak 1= ", rusak_1_net)
rusak_2_net = np.dot(rusak_2_weight_baru, pola_rusak_2) + u_delta_bias
print("targetnya pola U,net pola rusak 2= ", rusak_2_net)

# menghitung f(net) untuk pola rusak 1 dan 2
# target pola yang dituju: pola U
rusak_1_f_net = 0
if rusak_1_net >= 0:
    rusak_1_f_net = 1
else:
    rusak_1_f_net = -1
print("targetnya pola U,f(net) pola rusak 1= ", rusak_1_f_net)

rusak_2_f_net = 0
if rusak_2_net >= 0:
    rusak_2_f_net = 1
else:
    rusak_2_f_net = -1
print("targetnya pola U,f(net) pola rusak 2= ", rusak_2_f_net)

# penarikan kesimpulan
hasil_rusak_1 = ""
if rusak_1_f_net == target_pola_u:
    hasil_rusak_1 = "Pola rusak 1 dikenali model Hebb sebagai pola U"
else:
    hasil_rusak_1 = "Pola rusak 1 tidak dikenali model Hebb sebagai pola U"
print("targetnya pola U,hasil pengenalan pola rusak 1= ", hasil_rusak_1)

hasil_rusak_2 = ""
if rusak_2_f_net == target_pola_u:
    hasil_rusak_2 = "Pola rusak 2 dikenali model Hebb sebagai pola U"
else:
    hasil_rusak_2 = "Pola rusak 2 tidak dikenali model Hebb sebagai pola U"
print("targetnya pola U,hasil pengenalan pola rusak 2= ", hasil_rusak_2)
