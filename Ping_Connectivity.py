import pandas as pd
import subprocess
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize Tkinter root and hide the main window
Tk().withdraw()

# Prompt user to select the input Excel file
print("Please select the input Excel file containing IP addresses.")
input_file = askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])

# Check if a file was selected
if not input_file:
    print("No file selected. Exiting.")
    exit()

# Read IP addresses from the selected Excel file
df = pd.read_excel(input_file)

# Ensure 'IP Address' column exists
if 'IP Address' not in df.columns:
    raise ValueError("Excel file must contain a column named 'IP Address'")

# Create a list to store results
results = []

# Ping each IP address
for ip in df['IP Address']:
    try:
        # Ping command for Windows ('-n 1' sends only 1 ping packet)
        response = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True)

        # Check if ping was successful
        if 'TTL=' in response.stdout:
            results.append([ip, 'Success'])
        else:
            results.append([ip, 'Failure'])

    except Exception as e:
        results.append([ip, f'Error: {e}'])

# Create a DataFrame for results
result_df = pd.DataFrame(results, columns=['IP Address', 'Ping Result'])

# Save results to a new Excel file
output_file = 'ping_results.xlsx'  # Replace with your desired output file path
result_df.to_excel(output_file, index=False)

print(f"Ping results saved to {output_file}")
