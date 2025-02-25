trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

trips = {
    "miles" : trip_durations,
    "fares": trip_fares
}
trips["miles"]
trip_num = (int(input("What trip do you want?:")))
print(f"Duration: {trips["miles"][trip_num - 1]} hours")
print(f"Cost: ${trips["fares"][trip_num - 1]}")