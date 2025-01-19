# Databricks notebook source
# Importing necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, first, col, round

# Initialize Spark session
spark = SparkSession.builder.appName("ExchangeRateETL").getOrCreate()

# Load data from the 'bronze' layer
df_bronze = spark.read.parquet('dbfs:/databricks-results/bronze/exchange_rate/*/*/*')

# Filter for specific currencies (USD, EUR, GBP)
currency = ['USD', 'EUR', 'GBP']
df_currency = df_bronze.filter(df_bronze.currency.isin(currency))

# Convert the 'date' column to date format
df_currency = df_currency.withColumn('date', to_date(df_currency.date))

# Group by 'date' and pivot the 'currency' column to get the exchange rates
results_conversion_rate = df_currency.groupBy('date').pivot('currency').agg(first('rate')).orderBy('date', ascending=False)

# Select the results and convert the rates to real values (1 / rate)
results_real_values = results_conversion_rate.select('*')
for curr in currency:
    # Convert the exchange rates to real values by inverting the rates
    results_real_values = results_real_values.withColumn(curr, round(1 / col(curr), 4))

# Coalesce the DataFrame into one partition to avoid multiple output files
results_conversion_rate = results_conversion_rate.coalesce(1)
results_real_values = results_real_values.coalesce(1)

# Save the conversion rates to the 'silver' layer in CSV format
results_conversion_rate.write.format('csv').mode('overwrite').option('header', 'true').save('dbfs:/databricks-results/silver/exchange_rate/convection_rate')

# Save the real values to the 'silver' layer in CSV format
results_real_values.write.format('csv').mode('overwrite').option('header', 'true').save('dbfs:/databricks-results/silver/exchange_rate/real_values')

# Print a message indicating that the transformation is complete and files have been saved
print("Transformation completed and files saved successfully!")

