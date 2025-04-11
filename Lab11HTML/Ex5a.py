import requests

# Step 1: Define the API endpoint URL
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# Step 2: Make the GET request
response = requests.get(url)

# Step 3: Convert the response to JSON (list of records)
data = response.json()

# Step 4: Print the data
print("Response JSON:")
for record in data:
    print(record)

# Step 5: Identify the format
print("\nData Format: This is a list of dictionaries (JSON objects). Each dictionary represents a driver_type and its count.")
