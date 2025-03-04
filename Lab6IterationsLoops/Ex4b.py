sample_fares = [8.60, 5.75, 13.25, 21.21]

messages = [
    f"${round(fare, 2)} - This fare is high!" if fare > 12 
    else f"${round(fare, 2)} - This fare is low." 
    for fare in sample_fares
]

print("\n".join(messages))
