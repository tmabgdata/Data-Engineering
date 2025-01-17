# Databricks notebook source
import requests
from pyspark.sql.functions import lit

# COMMAND ----------

def get_exchange_rate(date, base='BRL'):

    url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"

    headers= {
    "apikey": "P6zxgJE2JKA3wYbzQyyw5fOWxYCHDf9o"
    }

    params = {'base':base}

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    return response.json()

# COMMAND ----------

def extract_exchange_rate(data_json):
    tuple_data = [(currency, float(rate)) for currency, rate in data_json['rates'].items()]
    return tuple_data

# COMMAND ----------

def save_file_parquet(get_exchange_rate):
    year, mounth, day = get_exchange_rate['date'].split('-')
    path = f'dbfs:/databricks-results/bronze/exchange_rate/{year}/{mounth}/{day}'
    response = extract_exchange_rate(get_exchange_rate)
    df_conversions = spark.createDataFrame(response, schema='currency string, rate double')
    df_conversions = df_conversions.withColumn('date', lit(f'{year}-{mounth}-{day}'))
    df_conversions.write.format('parquet').mode('overwrite').save(path)

    print(f'Data saved in {path}')

# COMMAND ----------

cotations = get_exchange_rate('2024-10-22')
save_file_parquet(cotations)
