# List of sample fares
sample_fares = [8.60, 5.75, 13.25, 21.21]

# Iterate through each fare in the list
for fare in sample_fares:
    if fare > 12:  # Check if the fare is greater than 12
        print(f"${fare:.2f} - This fare is high!")  
    else:
        print(f"${fare:.2f} - This fare is low.")  