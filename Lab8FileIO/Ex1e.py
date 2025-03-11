import os  

filename = "names.txt_bad"  

if os.path.exists(filename) and os.access(filename, os.R_OK):
    try:
        with open(filename, "r") as file_obj:
            line = file_obj.readline()
            while line:
                print(line.strip())
                line = file_obj.readline()

        with open(filename, "r") as file_obj:
            name_count = sum(1 for _ in file_obj)

        print(f'There are {name_count} names')

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Error: The file '{filename}' does not exist or is not readable.")

