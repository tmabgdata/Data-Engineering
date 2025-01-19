
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'tmabigdata',  # Owner of the DAG
    'depends_on_past': False,  # Avoids dependency on past runs
    'email_on_failure': False,  # Disable email notifications on failure
    'email_on_retry': False,  # Disable email notifications on retry
    'retries': 1,  # Retry once in case of failure
    'retry_delay': timedelta(minutes=5),  # Delay between retries
}

# Function to check if the data exists in the bronze layer on DBFS
def check_data_availability():
    # Path in DBFS where the data is stored (adjust the path as needed)
    data_path = "/dbfs/databricks-results/bronze/exchange_rate/"  # Adjust this path based on your directory structure
    try:
        # Using dbutils.fs to list the files in the bronze directory
        files = dbutils.fs.ls(data_path)
        if len(files) > 0:
            return True  # Data exists
        else:
            return False  # No data found
    except Exception as e:
        print(f"Error checking data in the bronze layer: {str(e)}")
        return False  # Error occurred during check

# Define the DAG
with DAG(
    'run_elt_notebook',  # DAG ID
    default_args=default_args,  # Default arguments for the DAG
    description='Run ELT notebook in Databricks',  # Description of the DAG
    schedule_interval='0 9 * * *',  # Runs every day at 9 AM
    start_date=datetime(2024, 11, 25),  # Start date of the DAG
    catchup=False,  # Avoids backfilling
) as dag_run_extracting_notebook:

    # Task to check if the data is available
    check_data = PythonOperator(
        task_id='check_data_availability',  # Task ID
        python_callable=check_data_availability  # Function to call
    )

    # Task to trigger the data extraction notebook if data is not available
    data_extracting = DatabricksRunNowOperator(
        task_id='extracting_fees',  # Task ID
        databricks_conn_id='databricks_default',  # Ensure the connection ID is correct
        job_id=967024990772222,  # Replace with your Databricks Job ID for extraction
        notebook_params={
            'execution_date': "{{ execution_date.strftime('%Y-%m-%d') }}"  # Passing the execution date in the format YYYY-MM-DD
        }
    )

    # Task to trigger the data transformation notebook (without parameters)
    data_transforming = DatabricksRunNowOperator(
        task_id='transforming_data',  # Task ID
        databricks_conn_id='databricks_default',  # Ensure the connection ID is correct
        job_id=533359294414436  # Replace with your Databricks Job ID for transformation
    )

    # Task to trigger the data report notebook
    sending_report = DatabricksRunNowOperator(
        task_id='sending_report',  # Task ID
        databricks_conn_id='databricks_default',  # Ensure the connection ID is correct
        job_id=280491257357132  # Replace with your Databricks Job ID for transformation
    )

    # Conditional execution: If the data exists, run the transformation task, else run the extraction task
    check_data >> [data_extracting, data_transforming]

    # Execution order:
    # If data is available, transformation task will run.
    # If data is not available, extraction task will run followed by transformation.
    data_extracting >> data_transforming >> sending_report