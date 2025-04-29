import json
import matplotlib.pyplot as plt

with open("trips_from_area8.json", "r") as f:
    data = json.load(f)

fares = []
trip_miles = []

for trip in data:
    try:
        fare = float(trip.get("fare", 0))
        miles = float(trip.get("trip_miles", 0))
        fares.append(fare)
        trip_miles.append(miles)
    except (ValueError, TypeError):
        continue  # Skip bad records

plt.figure(figsize=(10, 6))
plt.scatter(fares, trip_miles, alpha=0.6, color='green')
plt.title("Fare vs Trip Miles Scatter Plot")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.grid(True)
plt.tight_layout()
plt.show()
