# Define a list of test cases (list of lists)
test_cases = [
    [],                          # Fewer than 5 elements
    [1, 2],                     # Fewer than 5 elements
    ["apple", "banana", "cherry", "date"],  # Fewer than 5 elements
    [1, 2, 3, 4],              # Fewer than 5 elements
    [5, 6, 7, 8, 9],           # Exactly 5 elements
    ["x", "y", "z", 10, 20, 30, 40],  # Between 5 and 10 elements
    [True, False, None, "hello", 3.14, "world"], # Exactly 6 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Exactly 10 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # More than 10 elements
]

# Check list lengths and print results
for case in test_cases:
    length = len(case)
    if length < 5:
        message = "The list has fewer than 5 elements."
    elif 5 <= length <= 10:
        message = "The list has between 5 and 10 elements."
    else:
        message = "The list has more than 10 elements."
    
    print(f"List: {case} | Length: {length} | Message: {message}")
