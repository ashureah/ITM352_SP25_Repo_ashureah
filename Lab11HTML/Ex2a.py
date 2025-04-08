import ssl
import pandas as pd

# Disable SSL certificate verification (not for production)
ssl._create_default_https_context = ssl._create_unverified_context

# URL with interest rate data
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Read HTML tables from the URL (requires 'lxml' parser)
tables = pd.read_html(url)

# Let's say you want to print all tables found first
print(f"Found {len(tables)} tables")

# View the columns of the first table
df = tables[0]
print("Columns in the table:")
print(df.columns)
