# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_input = input("Enter a value to append to the tuple: ")

try:
    data.append(user_input)  # This will fail
except AttributeError:
    print("Tuples are immutable. Creating a new tuple instead.")
    data = data + (user_input,)  # Creating a new tuple by adding the input

# Print the updated tuple
print("Updated tuple:", data)
