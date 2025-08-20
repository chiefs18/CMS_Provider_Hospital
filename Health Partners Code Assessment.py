
# Import requests to handle HTTP requests
# Import re for regular expressions
# Import pandas for data manipulation
# Import StringIO to handle string data as file-like object
import requests, re
import pandas as pd
from io import StringIO

# Fetch the CSV file from the given URL
# Define the source file URL
sourceFile = "https://data.cms.gov/provider-data/sites/default/files/resources/893c372430d9d71a1c52737d01239d47_1753409109/Hospital_General_Information.csv"
# Make a GET request to fetch the CSV data
csvGet = requests.get(sourceFile)
# Assign text response to csvData
csvData = StringIO(csvGet.text)
# Read the CSV data into a pandas DataFrame
df = pd.read_csv(csvData, dtype=str)

# Clean the column names by removing special characters, converting to lowercase, and replacing spaces with underscores
# Create a new dictionary to hold cleaned column names
c_new = {}

# Iterate through each column name in the DataFrame and convert it to a cleaned format
for c in df.columns:
    c_new[c] = re.sub(r'[^\w\s]', '', c).strip().lower().replace(' ', '_')

# Update the DataFrame's columns with the cleaned names by assigning the new dictionary values
df.columns = c_new.values()

# Save the cleaned DataFrame to a CSV file
df.to_csv('C:\\Hospitals.csv', index=False)