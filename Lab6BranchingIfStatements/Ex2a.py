# Define a list with different values
list = [1, "apple", 3.14, True, "banana", 42]  # Example list

# Check the length of the list and print messages accordingly
if len(list) < 5:
    print("The list has fewer than 5 elements.")
elif 5 <= len(list) <= 10:
    print("The list has between 5 and 10 elements.")
else:
    print("The list has more than 10 elements.")

# Print the list and its length for reference
print("List:", list)
print("Length of list:", len(list))
