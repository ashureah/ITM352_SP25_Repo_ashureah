# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_input = input("Enter a value to append to the tuple: ")

# Create a new tuple using unpacking
data = (*data, user_input)

# Print the updated tuple
print("Updated tuple:", data)
