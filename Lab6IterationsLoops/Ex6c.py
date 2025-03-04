# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_input = input("Enter a value to append to the tuple: ")

try:
    data.append(user_input)  # This will cause an error
except AttributeError as e:
    print(f"Error: {e}")
    print("Tuples are immutable; you cannot append to them.")
