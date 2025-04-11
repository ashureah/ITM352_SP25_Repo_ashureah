# Step 1: Import necessary libraries
from sodapy import Socrata
import pandas as pd

# Step 2: Create a Socrata client (no app token required for public datasets)
client = Socrata("data.cityofchicago.org", None)

# Step 3: Fetch the first 500 records from the dataset rr23-ymwb (passenger vehicle licenses)
results = client.get("rr23-ymwb", limit=500)

# Step 4: Convert the JSON response to a pandas DataFrame
df = pd.DataFrame.from_records(results)

# Step 5: Inspect the first few rows
print(df.head())
