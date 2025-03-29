import gdown
import pandas as pd

# Google Drive file ID
file_id = '1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex'
url = f'https://drive.google.com/uc?id={file_id}'

# Download the file
output = 'downloaded_file.csv'
gdown.download(url, output, quiet=False)

# Read it into a DataFrame
df = pd.read_csv(output)

# Show dimensions and first 10 rows
print("DataFrame dimensions:", df.shape)
print("\nFirst 10 rows:")
print(df.head(10))

