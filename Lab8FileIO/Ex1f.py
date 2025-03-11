import os  

filename = "names.txt"

# Append a new name to the file
if os.path.exists(filename) and os.access(filename, os.W_OK):
    try:
        with open(filename, "a") as file_obj:
            file_obj.write("\nFuller, Ashureah") 

        with open(filename, "r") as file_obj:
            content = file_obj.read()
            print(content)

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Error: The file '{filename}' does not exist or is not writable.")
