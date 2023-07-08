import numpy as np
# bobot/W dan threshold/T
weight1=1
weight2=1
tetha=2

# tabel kebenaran
kolom_x1=np.array([0,0,1,1])
kolom_x2=np.array([0,1,0,1])
kolom_y=np.array([0,0,0,1])

# mencari nilai net
net=(weight1*kolom_x1+weight2*kolom_x2)
print("Net= ",net)

# mencari nilai y_net
y_net=(net>=tetha).astype(int)
print("y_net= ",y_net)

# membandingkan nilai y_net dan net