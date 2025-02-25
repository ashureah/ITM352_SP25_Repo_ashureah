def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def test_determine_progress(progress_function):

    assert progress_function(0, 0) == "Get going!", "Test Case 1 Failed"

    # Test Case 2: "On your way!" (0.25 <= hits/spins < 0.5)
    assert progress_function(1,5) == "On your way!", "Test Case 2 Failed"

    # Test Case 3: "Almost there!" (hits/spins >= 0.5 but hits < spins)
    assert progress_function(1,1) == "Almost there!", "Test Case 3 Failed"

    # Test Case 4: "You win!" (hits >= spins)
    assert progress_function(5, 10) == "You win!", "Test Case 4 Failed"

    print("All test cases passed!")


test_determine_progress(determine_progress1)
