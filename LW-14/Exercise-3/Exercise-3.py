# Author: Natan Nedaikhlib

import json
import matplotlib.pyplot as plt

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
        return {}
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
        return {}

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

def display_json(countries):
    """
    Function to display the contents of the JSON file on the screen.
    """
    if not countries:
        print("No data to display.")
        return
    for country in countries:
        print(f"Country Name: {country['name']}, Population: {country['population']} million, Area: {country['area']} thousand sq.km")

def add_record(countries):
    """
    Function to add a new record to the JSON file.
    """
    name = input("Enter the country name: ").strip()
    if any(country['name'].lower() == name.lower() for country in countries):
        print("A country with this name already exists.")
        return countries
    try:
        population = float(input("Enter the population (in millions): ").strip())
        area = float(input("Enter the area (in thousands of sq.km): ").strip())
    except ValueError:
        print("Error: Invalid input for population or area.")
        return countries
    new_country = {
        "name": name,
        "population": population,
        "area": area
    }
    countries.append(new_country)
    print(f"Country '{name}' successfully added.")
    return countries

def delete_record(countries):
    """
    Function to delete a record from the JSON file.
    """
    name = input("Enter the country name to delete: ").strip()
    for country in countries:
        if country['name'].lower() == name.lower():
            countries.remove(country)
            print(f"Country '{name}' successfully deleted.")
            return countries
    print(f"Country '{name}' not found.")
    return countries

def search_data(countries):
    """
    Function to search for data in the JSON file by one of the selectable fields.
    """
    if not countries:
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
        results = [country for country in countries if query.lower() in country['name'].lower()]
    else:
        try:
            query = float(query)
            results = [country for country in countries if country[field] == query]
        except ValueError:
            print("Error: Please enter a numeric value for population or area.")
            return
    if results:
        print("Search Results:")
        for country in results:
            print(f"Country Name: {country['name']}, Population: {country['population']} million, Area: {country['area']} thousand sq.km")
    else:
        print("No data found.")

def find_max_density(countries):
    """
    Function to determine the country with the highest population density.
    """
    if not countries:
        print("No data available for analysis.")
        return
    max_density = 0
    country_with_max_density = ""
    for country in countries:
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

def plot_pie_chart(countries):
    """
    Function to plot a pie chart showing the population distribution among countries.
    """
    if not countries:
        print("No data available to plot.")
        return
    # Extract country names and populations
    country_names = [country['name'] for country in countries]
    populations = [country['population'] for country in countries]
    
    # Calculate total population
    total_population = sum(populations)
    
    # Calculate percentages
    percentages = [(pop / total_population) * 100 for pop in populations]
    
    # Define colors
    colors = plt.cm.Paired(range(len(countries)))
    
    # Plot pie chart
    plt.figure(figsize=(8,8))
    patches, texts, autotexts = plt.pie(percentages, labels=country_names, colors=colors, autopct='%1.1f%%', startangle=140)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    
    # Add a title
    plt.title('Population Distribution Among Countries')
    
    # Customize font size of labels
    plt.setp(texts, fontsize=12)
    plt.setp(autotexts, fontsize=12, weight='bold')
    
    # Display the plot
    plt.show()

def main():
    """
    Main function that organizes the interactive menu for the user.
    """
    file_path = 'countries.json'
    data = load_json(file_path)
    
    # Отримання списку країн з ключа "countries"
    countries = data.get('countries', [])
    
    while True:
        print("\n--- Menu ---")
        print("1. Display JSON file contents")
        print("2. Add a new record")
        print("3. Delete a record")
        print("4. Search data by field")
        print("5. Determine the country with the highest population density")
        print("6. Plot Population Distribution Pie Chart")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()
        if choice == '1':
            display_json(countries)
        elif choice == '2':
            countries = add_record(countries)
            # Оновлюємо ключ "countries" у даних
            data['countries'] = countries
            save_json(file_path, data)
        elif choice == '3':
            countries = delete_record(countries)
            # Оновлюємо ключ "countries" у даних
            data['countries'] = countries
            save_json(file_path, data)
        elif choice == '4':
            search_data(countries)
        elif choice == '5':
            find_max_density(countries)
        elif choice == '6':
            plot_pie_chart(countries)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
