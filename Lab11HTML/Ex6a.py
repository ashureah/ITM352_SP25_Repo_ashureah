import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the webpage
url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find the table (usually has a recognizable class or structure)
table = soup.find("table")  # If there are multiple tables, specify the class or id

# Step 4: Extract each row
rows = table.find_all("tr")

# Step 5: Parse each row into a list of values
rate_data = []
for row in rows:
    cols = row.find_all(["th", "td"])  # Include both header and data cells
    cols = [col.get_text(strip=True) for col in cols]
    if cols:
        rate_data.append(cols)

# Output the extracted rate table
for row in rate_data:
    print(row)
