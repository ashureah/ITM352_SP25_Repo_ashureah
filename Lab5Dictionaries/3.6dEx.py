trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = [6.25, 5.25, 10.50, 8.05]
trips = dict(zip(trip_durations, trip_fares))
print(trips)

third_trip_duration = trip_durations[2] 
print(f"Duration: {third_trip_duration} hours")
print(f"Cost: ${trips[third_trip_duration]}")