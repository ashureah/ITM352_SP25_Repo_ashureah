import pandas as pd

url = "https://drive.google.com/file/d/1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus/view?usp=sharing"


df = pd.read_json(url)

print("Summary Statistics:\n", df.describe(include=["fare"]))


print("\nMedian Values:\n", df.median())
