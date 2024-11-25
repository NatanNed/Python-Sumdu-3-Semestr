# Author: Natan Nedaikhlib

import pandas as pd
import matplotlib.pyplot as plt
import os

def read_data():
    """
    Reads the CSV file and returns a DataFrame.
    """
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the CSV file
    filename = os.path.join(script_dir, 'comptagevelo2017.csv')
    try:
        # Read the CSV without parsing dates
        df = pd.read_csv(filename)
        # Drop the unnamed column
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        # Parse the 'Date' column with dayfirst=True
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        # Convert cyclist count columns to numeric
        for col in df.columns[1:]:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        print("Data successfully read from the file.")
        return df
    except Exception as e:
        print(f"Error reading data: {e}")
        return pd.DataFrame()

def process_data(df):
    """
    Processes the data and determines the most popular month among cyclists.
    """
    if df.empty:
        print("The DataFrame is empty.")
        return

    # Add a 'Month' column
    df['Month'] = df['Date'].dt.month

    # Sum the number of cyclists for each day
    df['Total Cyclists'] = df.iloc[:, 1:-1].sum(axis=1)

    # Sum the number of cyclists by month
    monthly_totals = df.groupby('Month')['Total Cyclists'].sum()

    # Determine the month with the highest number of cyclists
    max_month = monthly_totals.idxmax()
    max_value = monthly_totals.max()

    print(f"The most popular month among cyclists: Month {max_month} with {int(max_value)} cyclists.")
    return monthly_totals

def plot_monthly_usage(monthly_totals):
    """
    Plots bicycle path usage by month.
    """
    months = monthly_totals.index
    usage = monthly_totals.values

    plt.figure(figsize=(10,6))
    plt.bar(months, usage, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Number of Cyclists')
    plt.title('Bicycle Path Usage by Month in 2017')
    plt.xticks(months)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the program.
    """
    df = read_data()
    if df.empty:
        return
    monthly_totals = process_data(df)
    if monthly_totals is not None:
        plot_monthly_usage(monthly_totals)

if __name__ == "__main__":
    main()
