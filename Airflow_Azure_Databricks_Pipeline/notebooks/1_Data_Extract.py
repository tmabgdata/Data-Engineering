# Databricks notebook source
def get_exchange_rate(date, base='BRL'):

    import requests

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

get_exchange_rate('2024-06-16', 'BRL')

# COMMAND ----------


