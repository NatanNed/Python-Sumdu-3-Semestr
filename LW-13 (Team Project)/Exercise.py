# Author: Natan Nedaikhlib
import csv
import json
import sys

def create_csv_file(csv_filename):
    """
    Creates a CSV file and writes data into it.
    """
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write data rows
            writer.writerow({'id': '1', 'name': 'Alexander', 'age': '25'})
            writer.writerow({'id': '2', 'name': 'Maria', 'age': '30'})
            writer.writerow({'id': '3', 'name': 'Ivan', 'age': '22'})

    except IOError as e:
        print(f"Error writing to CSV file: {e}")
        sys.exit(1)

def convert_csv_to_json(csv_filename, json_filename):
    """
    Reads data from a CSV file and writes it to a JSON file.
    """
    data_list = []  # Initialize data_list here

    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        data = {'employees': data_list}  # Create the data dictionary after data_list is populated

        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)  # Dump 'data' instead of 'data_list'

    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error working with files: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unknown error: {e}")
        sys.exit(1)
        
# Студентка 2 Шаповал Анастасія         
def convert_json_to_csv(json_filename, csv_filename):
    """
    Reads data from a JSON file and writes it to a CSV file, adding new rows.
    """
    try:
        # Read data from the JSON file
        with open(json_filename, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

        # Check if 'employees' key exists in JSON data
        if 'employees' not in data:
            print(f"Key 'employees' not found in {json_filename}")
            sys.exit(1)

        employees = data['employees']

        # Define fieldnames for the CSV file
        fieldnames = ['id', 'name', 'age']

        # Write data to the CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write rows from JSON data
            for employee in employees:
                writer.writerow(employee)

            # Add new rows to the CSV file
            writer.writerow({'id': '4', 'name': 'Olga', 'age': '28'})
            writer.writerow({'id': '5', 'name': 'Sergey', 'age': '35'})

    except FileNotFoundError:
        print(f"File {json_filename} not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error working with files: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unknown error: {e}")
        sys.exit(1)        

if __name__ == "__main__":
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    updated_csv_filename = 'data_student2.csv'

    create_csv_file(csv_filename)
    convert_csv_to_json(csv_filename, json_filename)
    convert_json_to_csv(json_filename, updated_csv_filename)

    print(f"Data from {csv_filename} successfully converted to {json_filename}")
    print(f"Data from {json_filename} rewritten to {updated_csv_filename} with additional rows.")
