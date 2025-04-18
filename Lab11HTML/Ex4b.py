# Step 1: Import necessary libraries
from sodapy import Socrata
import pandas as pd

# Step 2: Create a Socrata client
client = Socrata("data.cityofchicago.org", None)

# Step 3: Fetch the first 500 records from the dataset
results = client.get("rr23-ymwb", limit=500)

# Step 4: Convert to DataFrame
df = pd.DataFrame.from_records(results)

# Step 5: Print vehicle make and fuel source
for index, row in df.iterrows():
    make = row.get("vehicle_make", "Unknown")
    fuel = row.get("vehicle_fuel_source", "Unknown")
    print(f"{make}: {fuel}")