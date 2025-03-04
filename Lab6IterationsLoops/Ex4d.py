def categorize_fares(fares):
    """Returns a list categorizing fares as high or low based on a $12 threshold."""
    return [f"${round(fare, 2)} - This fare is high!" if fare > 12 else f"${round(fare, 2)} - This fare is low." for fare in fares]

def test_categorize_fares():
    # Test Case 1: Mix of high and low fares
    assert categorize_fares([10, 15]) == ["$10 - This fare is low.", "$15 - This fare is high!"]

    # Test Case 2: All low fares
    assert categorize_fares([5, 8, 12]) == ["$5 - This fare is low.", "$8 - This fare is low.", "$12 - This fare is low."]

    # Test Case 3: All high fares
    assert categorize_fares([13, 20]) == ["$13 - This fare is high!", "$20 - This fare is high!"]

    # Test Case 4: Edge case - exactly $12
    assert categorize_fares([12]) == ["$12 - This fare is low."]

    # Test Case 5: Empty list (should return an empty list)
    assert categorize_fares([]) == []

    print("All test cases passed!")

test_categorize_fares()


