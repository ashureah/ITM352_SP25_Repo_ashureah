def convert_fahrenheit_to_celcius(fahrenheit_temp):
    #Convert Fahrenheit to Celcius. 
    celsius_temp = (fahrenheit_temp - 32) * (5/9)
    #Output conversion to user. 
    print(f"The temperature of {fahrenheit_temp}°F is equivalent to {celsius_temp:.2f}°C.")

fahrenheit_temp = float(input("Enter a temperature in Fahrenheit."))
convert_fahrenheit_to_celcius(fahrenheit_temp)