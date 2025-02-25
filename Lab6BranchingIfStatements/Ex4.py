def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap year"
    else:
        return "not a leap year"

# Get user input
year = int(input("Enter a year: "))
print(is_leap_year(year))
