# Description:
This Python script is designed to process a CSV file containing network traffic data and selectively extract specific columns. It utilizes the pandas library to efficiently manipulate the data and streamline the extraction process. By running this script, you can easily remove unnecessary columns from a CSV file and create a new CSV file with the desired subset of data.

# Features:
- Selectively extracts specific columns from a CSV file.
- Provides progress updates during script execution.
- Utilizes the pandas library for efficient data processing.
- Configurable input and output file paths.
- Easily customizable to suit your specific requirements

# Usage:
1) Prerequisites. 
   - Ensure you have Python (version 3.6 or higher) installed on your system.
   - Install the pandas library if you haven't already:
        pip install pandas
2) Clone the Repository:
    - Clone this repository to your local machine using your preferred method (HTTPS, SSH, GitHub CLI, etc.)..
3) Navigate to the Script:
    - Open a terminal or command prompt and navigate to the directory containing the cleanup.py.
4) Define Input and Output Paths:
    - In the script, modify the input_file and output_file paths to point to your source and desired output CSV files, respectively.
5) Run the Script:
    - Execute the script by running the following command in the terminal:
        python cleanup.py
    - This will initiate the process of reading the input CSV file, selecting the desired columns, and saving the updated data to the output CSV file.
6) Monitor Progress:
    - The script will display progress updates in the terminal as it performs each step of the data processing. This helps you keep track of the current execution status.
7) Review Output:
    - Once the script completes, navigate to the specified output_file path to find the new CSV file containing the selected columns.
8) Customization:
    - If needed, you can customize the columns_to_keep list to include the specific column names you want to extract.

# Example
Suppose you have a CSV file containing extensive network traffic data, and you only need specific columns such as application, device name, source IP, destination IP, and more. By using this script, you can efficiently extract these columns, removing unnecessary data and facilitating easier analysis.
