#Define what you what the user to be tasked to do or asked to do.
user_input = (input("Please enter a decimal number between 1 and 100: "))

# Convert "user_input" into a number and compute its square.
number = float(user_input)
squared_number = number ** 2

#Sets the ouput. What is going to be spit out to user. 
print(f"You entered the number: {number}")
print (f"The square of {number} is: {squared_number}")

