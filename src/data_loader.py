import pandas as pd

def load_data(file_path):
    """
    Load the financial news dataset.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['date'])
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

if __name__ == "__main__":
    # Test loading the data with a raw string path
    df = load_data(r'C:\Users\MMM\Documents\10 Academy File\KAIM-Week-12\data\raw_analyst_ratings.csv')
    print(df.head())
