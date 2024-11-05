import json

def load_json(file_path):
    """
    Function to load data from a JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
        return []

def save_json(file_path, data):
    """
    Function to save data to a JSON file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to '{file_path}'.")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

def display_json(data):
    """
    Function to display the contents of the JSON file on the screen.
    """
    if not data:
        print("No data to display.")
        return
    for country in data:
        print(f"Country Name: {country['name']}, Population: {country['population']} million, Area: {country['area']} thousand sq.km")

def add_record(data):
    """
    Function to add a new record to the JSON file.
    """
    name = input("Enter the country name: ").strip()
    if any(country['name'].lower() == name.lower() for country in data):
        print("A country with this name already exists.")
        return data
    try:
        population = float(input("Enter the population (in millions): ").strip())
        area = float(input("Enter the area (in thousands of sq.km): ").strip())
    except ValueError:
        print("Error: Invalid input for population or area.")
        return data
    new_country = {
        "name": name,
        "population": population,
        "area": area
    }
    data.append(new_country)
    print(f"Country '{name}' successfully added.")
    return data

def delete_record(data):
    """
    Function to delete a record from the JSON file.
    """
    name = input("Enter the country name to delete: ").strip()
    for country in data:
        if country['name'].lower() == name.lower():
            data.remove(country)
            print(f"Country '{name}' successfully deleted.")
            return data
    print(f"Country '{name}' not found.")
    return data

def search_data(data):
    """
    Function to search for data in the JSON file by one of the selectable fields.
    """
    if not data:
        print("No data available for searching.")
        return
    print("Field to search by:")
    print("1. Country Name")
    print("2. Population")
    print("3. Area")
    choice = input("Choose a field (1/2/3): ").strip()
    if choice == '1':
        field = 'name'
    elif choice == '2':
        field = 'population'
    elif choice == '3':
        field = 'area'
    else:
        print("Invalid choice.")
        return
    query = input("Enter the search value: ").strip()
    results = []
    if field == 'name':
        results = [country for country in data if query.lower() in country['name'].lower()]
    else:
        try:
            query = float(query)
            results = [country for country in data if country[field] == query]
        except ValueError:
            print("Error: Please enter a numeric value for population or area.")
            return
    if results:
        print("Search Results:")
        for country in results:
            print(f"Country Name: {country['name']}, Population: {country['population']} million, Area: {country['area']} thousand sq.km")
    else:
        print("No data found.")

def find_max_density(data):
    """
    Function to determine the country with the highest population density.
    """
    if not data:
        print("No data available for analysis.")
        return
    max_density = 0
    country_with_max_density = ""
    for country in data:
        try:
            density = country['population'] / country['area']  # Population in millions / Area in thousands sq.km
            if density > max_density:
                max_density = density
                country_with_max_density = country['name']
        except ZeroDivisionError:
            print(f"Error: Area for country '{country['name']}' is zero.")
    if country_with_max_density:
        result = {
            "country": country_with_max_density,
            "density": max_density  # Population per thousand sq.km
        }
        print(f"Country with the highest population density: {country_with_max_density} ({max_density:.2f} million/thousand sq.km)")
        save_json('max_density.json', result)
    else:
        print("Unable to determine the country with the highest population density.")

def main():
    """
    Main function that organizes the interactive menu for the user.
    """
    file_path = 'countries.json'
    data = load_json(file_path)
    while True:
        print("\n--- Menu ---")
        print("1. Display JSON file contents")
        print("2. Add a new record")
        print("3. Delete a record")
        print("4. Search data by field")
        print("5. Determine the country with the highest population density")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            display_json(data)
        elif choice == '2':
            data = add_record(data)
            save_json(file_path, data)
        elif choice == '3':
            data = delete_record(data)
            save_json(file_path, data)
        elif choice == '4':
            search_data(data)
        elif choice == '5':
            find_max_density(data)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
