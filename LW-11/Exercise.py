import csv
import os

def read_csv_file(file_path):
    """
    Function to read a CSV file and return its contents.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError:
        print(f"Error: Unable to open file '{file_path}'.")
        return []

def display_data(data):
    """
    Function to display the contents of the data on the screen.
    """
    if not data:
        print("No data to display.")
        return

    # Display headers
    headers = data[0].keys()
    print("\t".join(headers))

    # Display rows
    for row in data:
        print("\t".join([row[header] for header in headers]))

def search_country_data(data, country_name):
    """
    Function to search for data by country name.
    """
    results = [row for row in data if country_name.lower() in row['Country Name'].lower()]
    return results

def write_to_csv(file_path, data, headers):
    """
    Function to write data to a new CSV file.
    """
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Search results successfully written to '{file_path}'.")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")


# Define the input and output file paths using relative paths
input_file = 'inflation_data.csv'       # Input CSV file in the current directory
output_file = 'search_results.csv'      # Output CSV file will be created in the current directory

# Read data from the CSV file
data = read_csv_file(input_file)

# Display data on the screen
print("Contents of the CSV file:")
display_data(data)

# Prompt user for the country name
country_name = input("\nEnter the country name to search: ").strip()
if not country_name:
    print("Error: Country name cannot be empty.")

# Search for data by country name
search_results = search_country_data(data, country_name)

if not search_results:
    print(f"No data found for country '{country_name}'.")
else:
    print(f"\nSearch results for '{country_name}':")
    display_data(search_results)

    # Write search results to a new CSV file
    headers = data[0].keys()
    write_to_csv(output_file, search_results, headers)

