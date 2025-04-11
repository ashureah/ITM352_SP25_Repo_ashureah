import requests
import pandas as pd

# Step 1: API request
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

# Step 2: Convert response to JSON
records = response.json()

# Step 3: Convert to DataFrame
df = pd.DataFrame(records)

# Step 4: Rename columns
df.columns = ["driver_type", "count"]

# Step 5: Convert 'count' column to integer (since it was a string in JSON)
df["count"] = df["count"].astype(int)

# Step 6: Set index to driver_type
df.set_index("driver_type", inplace=True)

# Step 7: Print DataFrame
print(df)
