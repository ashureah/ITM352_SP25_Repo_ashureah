
age = 25  
weekday = "Thursday" 
matinee = False


if matinee:
    price = 5 if age >= 65 else 8
elif weekday == "Tuesday":
    price = 10
elif age >= 65:
    price = 8
else:
    price = 14

# Print values and final price
print("Age:", age)
print("Weekday:", weekday)
print("Matinee:", matinee)
print("Price:", price)
