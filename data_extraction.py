import pandas as pd

def load_data(csv_file):
    """
    Load data from a CSV file.
    """
    try:
        data = pd.read_csv(csv_file)
        print(f"Data loaded successfully from {csv_file}.")
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

if __name__ == "__main__":
    # Load the dataset
    data = load_data("data/sales_data.csv")
    print(data.head())  # Preview the data
