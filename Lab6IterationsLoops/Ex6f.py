# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_input = input("Enter a value to append to the tuple: ")

# Convert tuple to list, append the value, then convert back to tuple
data_list = list(data)
data_list.append(user_input)
data = tuple(data_list)

# Print the updated tuple
print("Updated tuple:", data)
