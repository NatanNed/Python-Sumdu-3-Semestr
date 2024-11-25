# Author: Natan Nedaikhlib

import pandas as pd
import matplotlib.pyplot as plt

def load_data(csv_file):
    """
    Loads data from a CSV file into a Pandas DataFrame.
    
    Parameters:
    - csv_file: Path to the CSV file.
    
    Returns:
    - DataFrame containing the data.
    """
    try:
        data = pd.read_csv(csv_file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The provided CSV file is empty.")
        exit(1)
    except pd.errors.ParserError:
        print("Error: The CSV file is malformed.")
        exit(1)

def preprocess_data(data, country1, country2):
    """
    Processes the DataFrame to extract years and indicator values for two countries.
    
    Parameters:
    - data: DataFrame containing the data.
    - country1: Name of the first country.
    - country2: Name of the second country.
    
    Returns:
    - years: List of years.
    - country1_data: List of indicator values for country1.
    - country2_data: List of indicator values for country2.
    """
    # Filter data for the specific indicator and countries
    indicator = "Out-of-school children of primary school age, both sexes (number)"
    filtered_data = data[
        (data['Series'] == indicator) & 
        (data['Country Name'].isin([country1, country2]))
    ]
    
    if filtered_data.empty:
        print("Error: No data found for the specified countries and indicator.")
        exit(1)
    
    # Pivot the data to have countries as columns and years as rows
    pivot_data = filtered_data.pivot(index='Year', columns='Country Name', values='2004 [YR2004]')
    
    # The above pivot uses '2004 [YR2004]' as a placeholder; adjust as needed
    # We'll dynamically select the year columns
    year_columns = [col for col in data.columns if '[YR' in col]
    pivot_data = filtered_data.pivot(index='Year', columns='Country Name', values=year_columns)
    
    # Flatten the multi-level columns if necessary
    if isinstance(pivot_data.columns, pd.MultiIndex):
        pivot_data.columns = [col[0] for col in pivot_data.columns]
    
    # Extract years and corresponding data
    years = sorted(pivot_data.index.tolist())
    country1_data = pivot_data[country1].tolist()
    country2_data = pivot_data[country2].tolist()
    
    return years, country1_data, country2_data

def plot_time_series(years, country1_data, country2_data, country1, country2):
    """
    Plots the time series data for two countries on the same graph.
    
    Parameters:
    - years: List of years
    - country1_data: List of indicator values for country1
    - country2_data: List of indicator values for country2
    - country1: Name of the first country
    - country2: Name of the second country
    """
    plt.figure(figsize=(12, 6))
    
    # Plotting data for the first country
    plt.plot(years, country1_data, linestyle='-', color='blue', linewidth=2, label=country1)
    
    # Plotting data for the second country
    plt.plot(years, country2_data, linestyle='-', color='green', linewidth=2, label=country2)
    
    # Labeling the axes
    plt.xlabel('Year')
    plt.ylabel('Number of Children Out of Primary School')
    
    # Adding a title to the graph
    plt.title('Trend of Children Out of Primary School (2004-2023)')
    
    # Adding a legend to distinguish between the two countries
    plt.legend()
    
    # Display grid for better readability
    plt.grid(True)
    
    # Save the plot as an image (optional)
    plt.savefig('time_series_plot.png')
    
    # Display the plot
    plt.tight_layout()
    plt.show()

def plot_bar_chart(latest_year, data, country1, country2):
    """
    Plots a bar chart comparing the indicator values of two countries for the latest year.
    
    Parameters:
    - latest_year: The most recent year in the dataset.
    - data: DataFrame containing the data.
    - country1: Name of the first country.
    - country2: Name of the second country.
    """
    # Filter data for the latest year
    filtered_data = data[
        (data['Series'] == "Out-of-school children of primary school age, both sexes (number)") & 
        (data['Year'] == latest_year) & 
        (data['Country Name'].isin([country1, country2]))
    ]
    
    if filtered_data.empty:
        print(f"Error: No data available for the year {latest_year} for the specified countries.")
        exit(1)
    
    # Extract values
    values = filtered_data['2004 [YR2004]'].values  # Adjust column name as needed
    
    # If '2004 [YR2004]' is not the correct column, find the correct one
    year_columns = [col for col in data.columns if f'[{latest_year}' in col]
    if not year_columns:
        print(f"Error: No data available for the year {latest_year}.")
        exit(1)
    value_col = year_columns[0]
    values = filtered_data[value_col].values
    
    # Data for plotting
    countries = [country1, country2]
    values = values.tolist()
    
    plt.figure(figsize=(8, 6))
    
    # Creating the bar chart
    bars = plt.bar(countries, values, color=['blue', 'green'])
    
    # Adding value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + max(values)*0.01, f'{yval}', ha='center', va='bottom')
    
    # Labeling the axes
    plt.xlabel('Country')
    plt.ylabel('Number of Children Out of Primary School')
    
    # Adding a title to the bar chart
    plt.title(f'Children Out of Primary School in {latest_year}')
    
    # Display grid for better readability
    plt.grid(axis='y')
    
    # Save the plot as an image (optional)
    plt.savefig('bar_chart_plot.png')
    
    # Display the plot
    plt.tight_layout()
    plt.show()

def get_user_input(available_countries):
    """
    Prompts the user to input two country names.
    
    Parameters:
    - available_countries: List of available country names in the dataset.
    
    Returns:
    - Tuple containing the names of the two countries.
    """
    print("\n--- Bar Chart Visualization ---")
    while True:
        country1 = input("Enter the name of the first country: ").strip()
        if country1 not in available_countries:
            print(f"'{country1}' is not available in the dataset. Please choose from: {', '.join(available_countries)}")
            continue
        break
    
    while True:
        country2 = input("Enter the name of the second country: ").strip()
        if country2 not in available_countries:
            print(f"'{country2}' is not available in the dataset. Please choose from: {', '.join(available_countries)}")
            continue
        break
    
    return country1, country2

def main():
    """
    Main function to execute the data visualization tasks.
    """
    # Path to the CSV file
    csv_file = 'children_out_of_school.csv'  # Replace with your actual CSV file path
    
    # Load the data
    data = load_data(csv_file)
    
    # Ensure 'Year' column exists
    if 'Year' not in data.columns:
        print("Error: The CSV file must contain a 'Year' column.")
        exit(1)
    
    # Display available countries
    available_countries = list(data['Country Name'].unique())
    available_countries = [country for country in available_countries if isinstance(country, str)]
    print(f"Available countries in the dataset: {', '.join(available_countries)}")
    
    # Define default countries
    default_country1 = 'Ukraine'
    default_country2 = 'United States'
    
    # Check if default countries are in the dataset
    if default_country1 not in available_countries or default_country2 not in available_countries:
        print("Error: Default countries not found in the dataset. Please check the CSV file.")
        exit(1)
    
    # Subtask 2.1: Plotting Time Series
    years, country1_data, country2_data = preprocess_data(data, default_country1, default_country2)
    plot_time_series(years, country1_data, country2_data, default_country1, default_country2)
    
    # Subtask 2.2: Plotting Bar Charts Based on User Input
    user_country1, user_country2 = get_user_input(available_countries)
    
    # Get the latest year in the dataset
    latest_year = data['Year'].max()
    
    plot_bar_chart(latest_year, data, user_country1, user_country2)

if __name__ == "__main__":
    main()
