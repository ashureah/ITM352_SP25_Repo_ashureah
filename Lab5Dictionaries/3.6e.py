trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = [6.25, 5.25, 10.50, 8.05]

trips = [{'duration': duration, 'cost': fare} for duration, fare in zip(trip_durations, trip_fares)]
print(trips)

third_trip = trips[2] 
print(f"Duration: {third_trip['duration']} hours")
print(f"Cost: ${third_trip['cost']}")
