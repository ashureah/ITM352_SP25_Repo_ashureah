import json
import matplotlib.pyplot as plt

with open("Trips_fri_trip_miles_gt1.json", "r") as f:
    data = json.load(f)

fares = []
tips = []

for trip in data:
    try:
        fare = float(trip.get("fare", 0))
        tip = float(trip.get("tips", 0))
        fares.append(fare)
        tips.append(tip)
    except (ValueError, TypeError):
        continue


print("Sample fares:", fares[:5])
print("Sample tips:", tips[:5])


plt.figure(figsize=(10, 6))
plt.scatter(fares, tips, alpha=0.6, color='blue')
plt.title("Fare vs Tip Scatter Plot")
plt.xlabel("Fare ($)")
plt.ylabel("Tip ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
