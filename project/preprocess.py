import pandas as pd
import numpy as np

# Data Files
yield_file = './data/yield_1982_2024.csv'
inflation_file = './data/inflation_1982_2024.csv'
gdp_file = './data/GDP_1982_2024.csv'
m_yield_file = './data/M_yield_1982_2024.csv'
recession_file = './data/recession_data.csv'
unemployment_file = './data/unemployment_1982_2024.csv'
industrial_file = './data/industrial_1982_2024.csv'


def process_yield_data(file_path, output_path):
    # Read the CSV file 
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    
    # Replace missing values (e.g., '.') with NaN
    df["T10Y3M"] = pd.to_numeric(df["T10Y3M"], errors="coerce")
    
    # Group by year and month, and calculate the monthly average
    df["Month"] = df["DATE"].dt.to_period("M")
    monthly_avg = df.groupby("Month")["T10Y3M"].mean().reset_index()
    
    # Convert the period to a datetime format for output
    monthly_avg["Month"] = monthly_avg["Month"].dt.to_timestamp()
    
    # Format the output as YYYY-MM-01 and round the average to 3 significant figures
    monthly_avg["FormattedDate"] = monthly_avg["Month"].dt.strftime("%Y-%m-01")
    monthly_avg["T10Y3M"] = monthly_avg["T10Y3M"].round(3)
    
    # Prepare the output in the desired format
    output_data = monthly_avg[["FormattedDate", "T10Y3M"]]
    output_data.columns = ["observation_date", "yield"]
    
    # Save to a new CSV file with the desired header
    output_data.to_csv(output_path, index=False)

    print("Processing complete. Output saved to:", output_path)

def gather_data(inflation_file, gdp_file, m_yield_file, recession_file, unemployment_file, industrial_file):
    # Merge all files to a final CSV file
    output_file = './data/processed_data.csv'
    # Read the CSV files
    inflation = pd.read_csv(inflation_file, parse_dates=["observation_date"])
    gdp = pd.read_csv(gdp_file, parse_dates=["observation_date"])
    m_yield = pd.read_csv(m_yield_file, parse_dates=["observation_date"])
    recession = pd.read_csv(recession_file, parse_dates=["observation_date"])
    unemployment = pd.read_csv(unemployment_file, parse_dates=["observation_date"])
    industrial = pd.read_csv(industrial_file, parse_dates=["observation_date"])

    # Merge the dataframes
    merged_data = inflation.merge(gdp, on="observation_date", how="inner")
    merged_data = merged_data.merge(m_yield, on="observation_date", how="inner")
    merged_data = merged_data.merge(unemployment, on="observation_date", how="inner")
    merged_data = merged_data.merge(industrial, on="observation_date", how="inner")

    merged_data = merged_data.merge(recession, on="observation_date", how="inner")

    merged_data.columns = ["date", "inflation", "gdp", "yield", "unemployment", "industrial", "recession"]

    # Save the merged data to a new CSV file
    merged_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # process_yield_data(yield_file, './data/processed_yield_data.csv')
    gather_data(inflation_file, gdp_file, m_yield_file, recession_file, unemployment_file, industrial_file)  