with open("names.txt", "r") as file_obj:
    line = file_obj.readline() 
    while line:  
        print(line.strip()) 
        line = file_obj.readline()  

with open("names.txt", "r") as file_obj:
    name_count = sum(1 for _ in file_obj) 

print(f'There are {name_count} names')
