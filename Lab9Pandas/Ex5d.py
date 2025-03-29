import gdown
import pandas as pd

file_id = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
url = f"https://drive.google.com/uc?id={file_id}"
output = "housing_data.csv"

gdown.download(url, output, quiet=False)

df = pd.read_csv(output)

print("Initial data types:\n", df.dtypes)

numeric_columns = ['units', 'sale_price', 'land_sqft', 'gross_sqft']
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nCleaned data types:\n", df.dtypes)

df_filtered = df[df['units'] >= 500] if 'units' in df.columns else df
columns_to_drop = ['id', 'borough', 'easement']
df_filtered = df_filtered.drop(columns=[col for col in columns_to_drop if col in df_filtered.columns])

df_filtered = df_filtered.dropna()
df_filtered = df_filtered.drop_duplicates()

print("\nFinal Cleaned and Filtered Data:\n", df_filtered.head())
print(f"\nFinal shape: {df_filtered.shape}")
