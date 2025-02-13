#Input these three strings: First Name, Middile Initial, and a Last Name using format ()

first_name = input ("First Name: ")
middle_initial = input ("Middle Initial: ")
last_name = input ("Last Name: ")

name_parts = [first_name, middle_initial, last_name]
full_name = "{} {} {}".format(*name_parts)  # Unpacking the list

print (full_name)