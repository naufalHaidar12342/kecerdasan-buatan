import numpy as np

# Define the input patterns
x0 = np.array([-1, -1])
x1 = np.array([-1, 1])
x2 = np.array([-1, -1])
x3 = np.array([1, -1])
x4 = np.array([-1, -1])
x5 = np.array([1, -1])
x6 = np.array([1, -1])
x7 = np.array([-1, -1])
x8 = np.array([1, -1])
x9 = np.array([-1, -1])  # Broken pattern

# Define the target patterns
t_pattern = np.array([-1, -1, -1, 1, -1, 1, 1, -1, 1])
u_pattern = np.array([-1, 1, -1, -1, 1, -1, -1, -1, -1])

# Initialize the weight matrix
W = np.zeros((2, 2))


# Define the activation function
def activation(x):
    return 1 if x >= 0 else -1


# Perform the Hebb learning algorithm
for x in [x0, x1, x2, x3, x4, x5, x6, x7, x8]:
    X = np.reshape(x, (2, 1))
    W += np.dot(X, X.T)

# Make a copy of the weight matrix
W_copy = np.copy(W)

# Test the learned weight matrix with T and U patterns
test_patterns = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
patterns_recognized = []
for pattern in test_patterns:
    y = np.dot(W, pattern)
    output = np.array([activation(val) for val in y])
    if np.array_equal(output, t_pattern) and "Pola T" not in patterns_recognized:
        patterns_recognized.append("Pola T")
    elif np.array_equal(output, u_pattern) and "Pola U" not in patterns_recognized:
        patterns_recognized.append("Pola U")

# Check if the broken pattern was recognized
if "Pola T" in patterns_recognized:
    print("Pola T dikenali.")
elif "Pola U" in patterns_recognized:
    print("Pola U dikenali.")
else:
    # Test the broken pattern with the preserved T and U patterns
    y_t = np.dot(W_copy, x9)
    output_t = np.array([activation(val) for val in y_t])

    y_u = np.dot(W_copy, np.flip(x9))
    output_u = np.array([activation(val) for val in y_u])

    if np.array_equal(output_t, t_pattern):
        print("Pola T dikenali.")
    elif np.array_equal(output_u, u_pattern):
        print("Pola U dikenali.")
    else:
        print("Pola rusak tidak dikenali.")
