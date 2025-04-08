import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the rate table (it's the first one on the page)
table = soup.find("table")

# Get all rows of the table (skip the header if needed)
rows = table.find_all("tr")

# Loop through the rows and extract bank name and current rates
for i, row in enumerate(rows[1:]):  # Skip header row with [1:]
    cols = row.find_all("td")
    if len(cols) >= 2:  # Ensure there's at least a bank name and one rate
        bank_name = cols[0].get_text(strip=True)
        rates = [col.get_text(strip=True) for col in cols[1:]]
        print(f"{bank_name}: {', '.join(rates)}")
