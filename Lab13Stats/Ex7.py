import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

with open("trips_from_area8.json", "r") as f:
    data = json.load(f)


fares = []
miles = []
dropoff_areas = []

for trip in data:
    try:
        fare = float(trip.get("fare", 0))
        trip_miles = float(trip.get("trip_miles", 0))
        dropoff_area = int(trip.get("dropoff_community_area", -1))

    
        if trip_miles > 0 and dropoff_area >= 0:
            fares.append(fare)
            miles.append(trip_miles)
            dropoff_areas.append(dropoff_area)
    except (ValueError, TypeError):
        continue

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(fares, miles, dropoff_areas, c='purple', alpha=0.6, marker='o')


ax.set_title("3D Plot: Fare vs Trip Miles vs Dropoff Area")
ax.set_xlabel("Fare ($)")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Community Area")

plt.tight_layout()
plt.show()
