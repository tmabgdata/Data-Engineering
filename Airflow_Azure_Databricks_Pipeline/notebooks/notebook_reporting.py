# Databricks notebook source
# Import necessary libraries
from slack_sdk import WebClient
import pyspark.pandas as ps

# Slack token and client setup
slack_token = ''
client = WebClient(token=slack_token)

# Retrieve the most recent CSV file from the Databricks file system
file_name = dbutils.fs.ls('dbfs:/databricks-results/silver/exchange_rate/real_values/')[-1].name
path = '../../dbfs/databricks-results/silver/exchange_rate/real_values/' + file_name

# Send the CSV file to the Slack channel
send_csv_file = client.files_upload_v2(
    channels='',  # Slack channel ID
    title='real values csv',  # Title for the uploaded file
    file=path,  # File path to upload
    filename=file_name,  # Filename displayed in Slack
    initial_comment='Following file in attachment'  # Comment for the file
)

# Read the CSV file into a pandas-on-Spark DataFrame
df_real_values = ps.read_csv('dbfs:/databricks-results/silver/exchange_rate/real_values/')

# Create a directory to store images if it doesn't already exist
!mkdir -p images

# Generate line plots for each currency and save them as images
for currency in df_real_values.columns[1:]:
    fig = df_real_values.plot.line(x='date', y=currency)  # Create the line plot
    fig.write_image(f'images/{currency}.png')  # Save the plot as an image

# Define a function to send images to Slack
def sending_images(quotation_currency):
    sending_images = client.files_upload_v2(
        channels='',  # Slack channel ID
        title='Sending Quotation Images',  # Title for the uploaded image
        file=f'./images/{quotation_currency}.png',  # Path to the image file
    )

# Send each currency image to the Slack channel
for currency in df_real_values.columns[1:]:
    sending_images(currency)

