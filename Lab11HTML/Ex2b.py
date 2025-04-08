import ssl
import pandas as pd

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# URL for October 2024 Treasury data
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Read the interest rate table
tables = pd.read_html(url)
df = tables[0]

# Make sure '1 Mo' column is numeric (in case it's a string)
df['1 Mo'] = pd.to_numeric(df['1 Mo'], errors='coerce')

# Loop through the DataFrame rows and print Date and 1 Mo interest rate
for index, row in df.iterrows():
    print(f"{row['Date']} - 1 Mo Rate: {row['1 Mo']}%")
