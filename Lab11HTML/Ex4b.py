# Check what the column names are to confirm field names
print(df.columns)

# Assuming relevant columns are named 'vehicle_make' and 'fuel_type'
# Drop rows where either value is missing to keep the list clean
vehicle_fuel_df = df[['vehicle_make', 'fuel_type']].dropna()

# Drop duplicates to get unique make-fuel_type pairs
unique_vehicles = vehicle_fuel_df.drop_duplicates()

# Print them
print(unique_vehicles)
