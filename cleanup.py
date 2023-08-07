#!/usr/bin/env python3

# import the pandas library
import pandas as pd

# Specify the file paths
input_file = r'C:\PROJECTS\input.csv'
output_file = r'C:\PROJECTS\output.csv'

# Specify the column names you want to keep
columns_to_keep = ['app', 'devname', 'dstintf', 'dstip', 'dstport', 'policyname', 'proto', 'service', 'srcintf', 'srcip']

# Read the CSV file into a DataFrame, specifying dtype as str
print("Reading input CSV file...")
df = pd.read_csv(input_file, dtype=str)

# Select the desired columns
print("Selecting desired columns...")
df = df[columns_to_keep]

# Save the updated DataFrame to a new CSV file
print("Saving updated DataFrame to output CSV file...")
df.to_csv(output_file, index=False)

print("Script completed.")
