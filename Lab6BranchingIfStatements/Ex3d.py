def determine_progress_no_if(hits, spins):
    progress_messages = ["Get going!", "On your way!", "Almost there!", "You win!"]
    
    # Avoid division by zero
    hits_spins_ratio = hits / spins if spins != 0 else 0  

    # Compute the index safely
    index = (spins > 0) * ((hits >= spins) * 3 or (hits_spins_ratio >= 0.5) * 2 or (hits_spins_ratio >= 0.25) * 1)

    return progress_messages[index]

# Test cases
print(determine_progress_no_if(0, 0))   # "Get going!"
print(determine_progress_no_if(2, 5))   # "On your way!"
print(determine_progress_no_if(5, 10))  # "Almost there!"
print(determine_progress_no_if(10, 10)) # "You win!"
