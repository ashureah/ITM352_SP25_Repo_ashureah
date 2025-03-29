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
    else:
        print(f"Warning: Column '{col}' not found in dataset.")


print("\nCleaned data types:\n", df.dtypes)


if 'units' in df.columns:
    df_filtered = df[df['units'] >= 500]
else:
    df_filtered = df

columns_to_drop = ['id', 'borough', 'easement']
df_filtered = df_filtered.drop(columns=[col for col in columns_to_drop if col in df_filtered.columns])

print("\nCleaned and Filtered Data:\n", df_filtered.head())