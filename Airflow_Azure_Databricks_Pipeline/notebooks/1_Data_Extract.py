# Databricks notebook source
import requests
from pyspark.sql.functions import lit
from datetime import datetime, timedelta

# Define a fixed execution date for testing outside of Airflow
execion_date = None

# Check if the code is being executed in Airflow
try:
    # The variable {{ ds }} will be automatically replaced in Airflow
    execion_date = "{{ ds }}"
except NameError:
    # If the code is not in Airflow, set a manual test date
    execion_date = '2024-12-01'  # Change this date to any necessary test value within the last 2 months

# If the execution is not in Airflow, the variable {{ ds }} will not be replaced
if execion_date == "{{ ds }}":
    execion_date = '2024-12-01'  # Ensure a default test date is set within the last 2 months

# Validate the execution_date parameter
try:
    exec_date_obj = datetime.strptime(execion_date, '%Y-%m-%d')
    print(f"Valid execution date: {exec_date_obj}")
except ValueError:
    raise ValueError(f"Invalid execution_date format: {execion_date}. Expected format: YYYY-MM-DD.")

# Validate the time range
max_date = datetime.today() - timedelta(days=60)  # Two months ago

# Check if the date is within the allowed range (maximum 2 months ago)
if exec_date_obj < max_date:
    raise ValueError(f"execution_date {execion_date} is out of the allowed range (max 2 months ago).")

# Function to get the exchange rate
def get_exchange_rate(date, base='BRL'):
    """
    Function that uses the API to get exchange rates.
    The URL includes the base parameter to choose the source currency.
    """
    url = f"https://api.apilayer.com/exchangerates_data/{date}?base={base}"
    headers = {"apikey": "P6zxgJE2JKA3wYbzQyyw5fOWxYCHDf9o"}
    
    # Make the GET request
    print(f"Fetching exchange rate data for date: {date}...")
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
    
    print(f"Data successfully obtained for date {date}.")
    return response.json()

# Function to extract exchange rates from JSON
def extract_exchange_rate(data_json):
    """
    Function that extracts exchange rates from the JSON returned by the API.
    """
    print(f"Extracting exchange rates...")
    return [(currency, float(rate)) for currency, rate in data_json['rates'].items()]

# Function to save data in Parquet format
def save_file_parquet(exchange_data):
    """
    Function that saves the extracted exchange rates in Parquet format in Databricks.
    """
    # Extract the date in the appropriate format
    year, month, day = exchange_data['date'].split('-')
    path = f'dbfs:/databricks-results/bronze/exchange_rate/{year}/{month}/{day}'
    print(f"Saving data to path: {path}...")

    # Extract exchange rates and create a DataFrame
    response = extract_exchange_rate(exchange_data)
    df_conversions = spark.createDataFrame(response, schema='currency string, rate double')
    df_conversions = df_conversions.withColumn('date', lit(f'{year}-{month}-{day}'))
    
    # Save the data in Parquet format
    df_conversions.write.format('parquet').mode('overwrite').save(path)
    print(f'Data saved to path {path}')

# Main processing
print("Starting the process...")

# Get exchange rates for the execution date
cotations = get_exchange_rate(execion_date)

# Save the data in Parquet
save_file_parquet(cotations)

print("Process completed.")
