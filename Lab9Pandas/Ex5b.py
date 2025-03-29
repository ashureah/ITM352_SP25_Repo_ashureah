import gdown
import pandas as pd

# Google Drive file ID and download URL
file_id = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file to local disk
output = "housing_data.csv"
gdown.download(url, output, quiet=False)

# Load the CSV into a DataFrame
df = pd.read_csv(output)

# Convert 'units' column to numeric
df['units'] = pd.to_numeric(df['units'], errors='coerce')

# Filter rows where units >= 500
df_filtered = df[df['units'] >= 500]

# Drop unnecessary columns
df_filtered = df_filtered.drop(columns=['id', 'borough', 'easement'], errors='ignore')

# Print first few rows of the filtered data
print(df_filtered.head())
