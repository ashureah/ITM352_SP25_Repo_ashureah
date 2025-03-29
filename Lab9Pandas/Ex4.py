import pandas as pd

file_path = "Taxi_Trips.json"
df = pd.read_json(file_path)

# Print summary statistics
print(df.describe())

print(df)

print("\nMedian fare:", df ["fare"].median())