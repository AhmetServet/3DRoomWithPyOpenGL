import subprocess
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import ast

# Get the full path of the profile_data file
profile_data_path = os.path.abspath("profile_data")
print(f"Full path of profile_data file: {profile_data_path}")

# Step 1: Start the Snakeviz server
print("Starting Snakeviz server...")
server_process = subprocess.Popen(
    ["snakeviz", profile_data_path],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Give the server time to start
time.sleep(3)

# Step 2: Fetch the data from the Snakeviz server
try:
    url = f"http://127.0.0.1:8080/snakeviz/{profile_data_path}"
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table in the HTML
    table = soup.find('table')
    # Find the JavaScript variable containing the table data
    script = soup.find('script', string=lambda text: text and 'var table_data =' in text)
    if script:
        script_content = script.string
        start_index = script_content.find('var table_data =') + len('var table_data =')
        end_index = script_content.find("];\n", start_index) + 1
        table_data_raw = script_content[start_index:end_index].strip()
        table_data = table_data_raw.encode('unicode_escape').decode('utf-8')
        table_data = ast.literal_eval(table_data)
    else:
        print("No JavaScript variable 'table_data' found.")
        raise ValueError("Could not extract the table data from JavaScript.")

    if table is None:
        print("No table found on the Snakeviz page.")
        raise ValueError("Could not extract the table.")

    # Extract table headers
    headers = [header.text for header in table.find_all('th')] + ["file_path"]

    # Step 3: Create a pandas DataFrame
    df = pd.DataFrame(table_data, columns=headers)
    df.drop(columns=["filename:lineno(function)"], inplace=True)
    df["file_path"] = df["file_path"].apply(lambda x: "".join(x.split("/")[-1]))
    df["ncalls"] = df["ncalls"].apply(lambda x: list(x)[0])

    # Save the DataFrame to a CSV file
    output_csv_path = "snakeviz_data.csv"
    df.to_csv(output_csv_path, index=False)
    print(f"Data saved to {output_csv_path}")

finally:
    # Step 4: Terminate the Snakeviz server
    print("Stopping Snakeviz server...")
    server_process.terminate()
    try:
        server_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        server_process.kill()
        print("Force killed the Snakeviz server.")


# analysis

# sort the data by the cumulative time
data = pd.read_csv("snakeviz_data.csv")

# Sort the data by 'tottime' column in descending order
data_sorted_tottime = data.sort_values(by='tottime', ascending=False)

# Exclude the first row of the sorted data
top_functions_tottime_excluded = data_sorted_tottime.iloc[1:11]

# Plot the total time excluding the first row -> exec functiono
plt.figure(figsize=(12, 6))
plt.barh(top_functions_tottime_excluded['file_path'], top_functions_tottime_excluded['tottime'], edgecolor='black')
plt.xlabel('Total Time (seconds)')
plt.ylabel('Function / File Path')
plt.title('Top 10 Most Time-Consuming Functions by Total Time (Excluding Top Entry)')
plt.gca().invert_yaxis()  # Invert y-axis to show the highest time first
plt.tight_layout()
plt.savefig('top_10_functions_tottime.png')