# Ping_Connectivity
Ping IP addresses in a provided list to determine if the IP address is reachable. Save output in a seperate excel indicating Success/Failure file indicating 


# IP Address Ping Checker

This Python script allows users to ping a list of IP addresses from an Excel file and outputs the results to a new Excel file, indicating whether each ping was successful or not.

## Features
- Prompts the user to select an Excel file containing IP addresses.
- Checks connectivity by pinging each IP address listed.
- Saves the results in a new Excel file, displaying "Success" for reachable IPs and "Failure" otherwise.

## Requirements
- **Python 3.x**
- **Netmiko**: For SSH connections.
- **pandas**: For Excel file manipulation.
- **openpyxl**: For reading/writing Excel files.
- **Tkinter**: For GUI creation.

**Packages**: Install required packages using `pip`:

  ```bash
  pip install pandas openpyxl netmiko tkinter
  ```


**Operating System:** This script is configured for Windows ping commands. Modify the ping command if running on other operating systems.

## Input File Format
The input Excel file should contain a column named IP Address listing the IPs to be pinged. 

Here is an example:

|IP Address  |
|------------|
|192.168.1.1 |
|192.168.1.2 |


## Usage
**Run the Script:** Open a terminal in the directory where the script is saved and execute:

```bash
python Ping_Connectivity.py
```

**Select Input File:** A file dialog will prompt you to select the Excel file containing the IP addresses.

**View Results:** The script will output results to a new Excel file named ping_results.xlsx, saved in the current directory, with columns for:

- **IP Address**
- **Ping Result** (Success, Failure, or Error)


## Example Output Excel File
The output file, ping_results.xlsx, will look like this:

|IP Address	 |Ping Result |
|------------|------------|
|192.168.1.1 |	Success   |
|192.168.1.2 |	Failure   |



## Troubleshooting
**Column Error:** If the selected Excel file does not have a column named IP Address, the script will raise an error.

**Permissions:** If running on Windows, you may need administrator permissions to run ping commands.

## License
This project is open-source and free to use.
