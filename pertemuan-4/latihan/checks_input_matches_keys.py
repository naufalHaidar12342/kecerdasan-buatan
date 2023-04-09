# define a dictionary of messages to print based on whether each input matches a key in the dictionary
messages = {
    True: "matches a key in the dictionary.",
    False: "doesn't match any key in the dictionary."
}

# define a dictionary
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# take two inputs from the user
input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")

# check if each input matches any key in the dictionary using a dictionary "switch"
for input_val in [input1, input2]:
    print(
        f"The {('first', 'second')[input_val == input2]} input {messages.get(input_val in my_dict.keys())}")


# manual way to check 2 inputs
# define a dictionary
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# take two inputs from the user
input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")

# check if the first input matches any key in the dictionary
if input1 in my_dict.keys():
    print("The first input matches a key in the dictionary.")
else:
    print("The first input doesn't match any key in the dictionary.")

# check if the second input matches any key in the dictionary
if input2 in my_dict.keys():
    print("The second input matches a key in the dictionary.")
else:
    print("The second input doesn't match any key in the dictionary.")
