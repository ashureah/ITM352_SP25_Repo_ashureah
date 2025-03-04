# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_input = input("Enter a value to append to the tuple: ")

# Attempt to append to the tuple (this will cause an error)
data.append(user_input)

# Print the updated tuple
print("Updated tuple:", data)
