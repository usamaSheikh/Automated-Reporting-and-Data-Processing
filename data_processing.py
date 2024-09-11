import pandas as pd

def process_data(data):
    """
    Process the sales data to calculate key metrics.
    """
    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Calculate total sales by region
    total_sales_by_region = data.groupby('region')['sales'].sum()

    # Calculate average monthly sales
    data['month'] = data['date'].dt.to_period('M')
    avg_monthly_sales = data.groupby('month')['sales'].mean()

    return total_sales_by_region, avg_monthly_sales

if __name__ == "__main__":
    from data_extraction import load_data

    # Load data
    data = load_data("data/sales_data.csv")
    
    if data is not None:
        # Process data
        total_sales_by_region, avg_monthly_sales = process_data(data)
        print("Total Sales by Region:\n", total_sales_by_region)
        print("Average Monthly Sales:\n", avg_monthly_sales)
