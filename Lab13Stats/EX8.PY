import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

# Drop rows with missing pickup or dropoff areas
df = df.dropna(subset=["pickup_community_area", "dropoff_community_area"])

# Convert areas to integers (if not already)
df["pickup_community_area"] = df["pickup_community_area"].astype(int)
df["dropoff_community_area"] = df["dropoff_community_area"].astype(int)

# Create a pivot table counting trips from each pickup to dropoff area
trip_matrix = pd.crosstab(df["pickup_community_area"], df["dropoff_community_area"])

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(trip_matrix, cmap="YlGnBu", annot=False, cbar=True)
plt.title("Heatmap of Taxi Trips: Pickup vs Dropoff Community Area")
plt.xlabel("Dropoff Community Area")
plt.ylabel("Pickup Community Area")
plt.tight_layout()
plt.show()
