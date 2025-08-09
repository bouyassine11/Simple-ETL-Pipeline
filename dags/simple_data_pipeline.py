from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.data_processor import process_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'simple_data_pipeline',
    default_args=default_args,
    description='A simple data processing pipeline',
    schedule_interval=timedelta(days=1),  # Runs daily
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['data_processing'],
) as dag:

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        op_kwargs={
            'input_path': '/opt/airflow/data/input/source_data.csv',
            'output_path': '/opt/airflow/data/output/processed_data.csv'
        }
    )

    # If you had multiple tasks, you could define dependencies here
    # task1 >> task2 >> task3
    process_data_task