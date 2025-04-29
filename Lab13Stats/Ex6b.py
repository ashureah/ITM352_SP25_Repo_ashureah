import json
import matplotlib.pyplot as plt


with open("Trips from area 8.json", "r") as f:
    data = json.load(f)

fares = []
trip_miles = []

for trip in data:
    try:
        fare = float(trip.get("fare", 0))
        miles = float(trip.get("trip_miles", 0))
        if miles > 0: 
            fares.append(fare)
            trip_miles.append(miles)
    except (ValueError, TypeError):
        continue


plt.figure(figsize=(10, 6))
plt.plot(fares, trip_miles, linestyle="none", marker="v", color="cyan", alpha=0.2)
plt.title("Fare vs Trip Miles (Filtered: Miles > 0)")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.grid(True)
plt.tight_layout()


plt.savefig("FaresXmiles.png")


plt.show()
