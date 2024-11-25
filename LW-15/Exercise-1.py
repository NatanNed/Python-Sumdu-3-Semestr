# Author: Natan Nedaikhlib

import json
import matplotlib.pyplot as plt
import pandas as pd

def display_all_countries(countries):
    """
    Displays all country data in the dictionary.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    print("\nAll Countries Data:")
    print("{:<15} {:<20} {:<20}".format("Country", "Population (M)", "Area (K sq km)"))
    print("-" * 55)
    for country, data in countries.items():
        print("{:<15} {:<20} {:<20}".format(country, data['population'], data['area']))

def add_country(countries):
    """
    Adds a new country to the dictionary.
    """
    try:
        name = input("\nEnter the country name: ").strip()
        if not name:
            print("Country name cannot be empty.")
            return countries
        if name in countries:
            print(f"Country '{name}' already exists in the dictionary.")
            return countries
        population = float(input("Enter the population (in millions): "))
        if population < 0:
            print("Population cannot be negative.")
            return countries
        area = float(input("Enter the area (in thousands of sq km): "))
        if area <= 0:
            print("Area must be greater than zero.")
            return countries
        density = population / area  # Calculate density
        countries[name] = {'population': population, 'area': area, 'density': density}
        print(f"Country '{name}' has been added successfully with a density of {density:.2f} million per thousand sq km.")
    except ValueError:
        print("Invalid input. Please enter numerical values for population and area.")
    return countries

def remove_country(countries):
    """
    Removes a country from the dictionary.
    """
    name = input("\nEnter the country name to remove: ").strip()
    if name in countries:
        del countries[name]
        print(f"Country '{name}' has been removed successfully.")
    else:
        print(f"Country '{name}' does not exist in the dictionary.")
    return countries

def display_sorted_countries(countries):
    """
    Displays countries sorted by their names.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    sorted_countries = sorted(countries.keys())
    print("\nCountries Sorted by Name:")
    print("{:<15} {:<20} {:<20}".format("Country", "Population (M)", "Area (K sq km)"))
    print("-" * 55)
    for country in sorted_countries:
        data = countries[country]
        print("{:<15} {:<20} {:<20}".format(country, data['population'], data['area']))

def find_max_density_country(countries):
    """
    Finds and displays the country with the highest population density.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    max_density = None
    max_density_country = None
    for country, data in countries.items():
        density = data['population'] / data['area']
        if (max_density is None) or (density > max_density):
            max_density = density
            max_density_country = country
    print("\nCountry with the Highest Population Density:")
    print(f"{max_density_country} with a density of {max_density:.2f} million per thousand sq km.")

def initialize_countries():
    """
    Initializes the country dictionary with predefined data, including density.
    """
    return {
        'CountryA': {'population': 50.0, 'area': 25.0, 'density': 2.0},
        'CountryB': {'population': 80.0, 'area': 40.0, 'density': 2.0},
        'CountryC': {'population': 30.0, 'area': 15.0, 'density': 2.0},
        'CountryD': {'population': 60.0, 'area': 30.0, 'density': 2.0},
        'CountryE': {'population': 90.0, 'area': 45.0, 'density': 2.0},
        'CountryF': {'population': 70.0, 'area': 35.0, 'density': 2.0},
        'CountryG': {'population': 20.0, 'area': 10.0, 'density': 2.0},
        'CountryH': {'population': 40.0, 'area': 20.0, 'density': 2.0},
        'CountryI': {'population': 100.0, 'area': 50.0, 'density': 2.0},
        'CountryJ': {'population': 55.0, 'area': 27.5, 'density': 2.0},
        # Adding more countries with varied densities
        'CountryK': {'population': 150.0, 'area': 50.0, 'density': 3.0},
        'CountryL': {'population': 10.0, 'area': 50.0, 'density': 0.2},
        'CountryM': {'population': 75.0, 'area': 15.0, 'density': 5.0},
    }

def get_country_data(num_countries):
    """
    Collects data for a specified number of countries from the user.
    """
    countries = {}
    for i in range(1, num_countries + 1):
        print(f"\nEnter details for country #{i}:")
        name = input("Country Name: ").strip()
        if not name:
            print("Country name cannot be empty. Skipping this entry.")
            continue
        if name in countries:
            print(f"Country '{name}' already exists. Skipping duplicate entry.")
            continue

        while True:
            try:
                population = float(input("Population (in millions): "))
                if population < 0:
                    print("Population cannot be negative. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for population.")
        
        while True:
            try:
                area = float(input("Area (in thousands of square km): "))
                if area <= 0:
                    print("Area must be greater than zero. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for area.")
        
        density = population / area
        countries[name] = {'population': population, 'area': area, 'density': density}
        print(f"Country '{name}' added successfully with a density of {density:.2f} million per thousand sq km.")
    return countries

def convert_dict_to_dataframe(countries):
    """
    Converts the country dictionary to a pandas DataFrame.
    """
    if not countries:
        print("\nThe country dictionary is empty. Cannot convert to DataFrame.")
        return pd.DataFrame()
    df = pd.DataFrame.from_dict(countries, orient='index')
    df.index.name = 'Country'
    df.reset_index(inplace=True)
    
    # Calculate 'density' if it doesn't exist
    if 'density' not in df.columns:
        df['density'] = df['population'] / df['area']
    
    return df

def perform_aggregation(df):
    """
    Performs aggregation on the DataFrame.
    """
    if df.empty:
        print("\nDataFrame is empty. Cannot perform aggregation.")
        return
    total_population = df['population'].sum()
    total_area = df['area'].sum()
    average_population = df['population'].mean()
    average_area = df['area'].mean()
    
    print("\n--- Aggregated Data ---")
    print(f"Total Population: {total_population} million")
    print(f"Total Area: {total_area} thousand sq km")
    print(f"Average Population: {average_population:.2f} million")
    print(f"Average Area: {average_area:.2f} thousand sq km")

def perform_grouping(df):
    """
    Performs grouping on the DataFrame.
    Groups countries based on population density categories.
    """
    if df.empty:
        print("\nDataFrame is empty. Cannot perform grouping.")
        return
    # Define density categories
    bins = [0, 0.5, 1.5, 2.5, 3.5, 100]  # Adjusted bins for better distribution
    labels = ['0-0.5', '0.5-1.5', '1.5-2.5', '2.5-3.5', '3.5+']
    df['Density Category'] = pd.cut(df['density'], bins=bins, labels=labels, right=False)
    
    # Explicitly set 'observed=False' to include all categories
    grouped = df.groupby('Density Category', observed=False).size().reset_index(name='Number of Countries')
    
    print("\n--- Grouping by Population Density Categories ---")
    print(grouped)

def display_dataframe(df):
    """
    Displays the DataFrame.
    """
    if df.empty:
        print("\nDataFrame is empty.")
        return
    print("\n--- Countries DataFrame ---")
    print(df)

def save_dataframe_to_csv(df):
    """
    Saves the DataFrame to a CSV file.
    """
    if df.empty:
        print("\nDataFrame is empty. Nothing to save.")
        return
    file_name = input("Enter the filename to save (e.g., countries.csv): ").strip()
    try:
        df.to_csv(file_name, index=False)
        print(f"DataFrame successfully saved to '{file_name}'.")
    except Exception as e:
        print(f"Error saving DataFrame: {e}")

def plot_population_bar_chart(countries):
    """
    Plots a bar chart of population for each country.
    """
    if not countries:
        print("\nThe country dictionary is empty. Cannot plot.")
        return
    df = convert_dict_to_dataframe(countries)
    plt.figure(figsize=(10,6))
    plt.bar(df['Country'], df['population'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Population (M)')
    plt.title('Population of Countries')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the country data management program.
    """
    countries = initialize_countries()
    while True:
        print("\n=== Country Data Management ===")
        print("1. Display all countries")
        print("2. Add a new country")
        print("3. Remove a country")
        print("4. Display countries sorted by name")
        print("5. Find country with highest population density")
        print("6. Enter data for new countries")
        print("7. Convert dictionary to DataFrame and display")
        print("8. Perform Aggregation")
        print("9. Perform Grouping")
        print("10. Save DataFrame to CSV")
        print("11. Plot Population Bar Chart")
        print("12. Exit")
        choice = input("Enter your choice (1-12): ").strip()

        if choice == '1':
            display_all_countries(countries)
        elif choice == '2':
            countries = add_country(countries)
        elif choice == '3':
            countries = remove_country(countries)
        elif choice == '4':
            display_sorted_countries(countries)
        elif choice == '5':
            find_max_density_country(countries)
        elif choice == '6':
            try:
                num_countries = int(input("\nHow many countries would you like to add? "))
                if num_countries <= 0:
                    print("Number of countries must be positive.")
                    continue
                new_countries = get_country_data(num_countries)
                countries.update(new_countries)
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        elif choice == '7':
            df = convert_dict_to_dataframe(countries)
            display_dataframe(df)
        elif choice == '8':
            df = convert_dict_to_dataframe(countries)
            perform_aggregation(df)
        elif choice == '9':
            df = convert_dict_to_dataframe(countries)
            perform_grouping(df)
        elif choice == '10':
            df = convert_dict_to_dataframe(countries)
            save_dataframe_to_csv(df)
        elif choice == '11':
            plot_population_bar_chart(countries)
        elif choice == '12':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
