import ssl
import urllib.request
from bs4 import BeautifulSoup

# Disable SSL verification (only for testing)
ssl._create_default_https_context = ssl._create_unverified_context

# URL of the page
url = "https://shidler.hawaii.edu/itm/people"

# Open and read the page content
response = urllib.request.urlopen(url)
html = response.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "lxml")  # You can also use "html.parser" if lxml isn't installed

# Print the type of the soup object
print("Type of soup object:", type(soup))

# Prettify (print a nicely indented version of the HTML)
print("\nFirst few lines of prettified HTML:\n")
print(soup.prettify()[:500])  # Just printing the first 500 characters
