# Step 1: Import necessary libraries
from sodapy import Socrata
import pandas as pd

# Step 2: Create a Socrata client
client = Socrata("data.cityofchicago.org", None)

# Step 3: Fetch the first 500 records from the dataset
results = client.get("rr23-ymwb", limit=500)

# Step 4: Convert to DataFrame
df = pd.DataFrame.from_records(results)

# Group by fuel type and count the number of vehicles per fuel source
fuel_counts = df.groupby("vehicle_fuel_source")["vehicle_make"].count().reset_index()

# Rename columns for clarity
fuel_counts.columns = ["Fuel Source", "Number of Vehicles"]

# Print the result
print(fuel_counts)
