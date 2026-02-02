from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from tasks.download import download_and_unzip
from tasks.load_postgres import load_csv_to_postgres
import os


PG_CONFIG = {
    "user": os.getenv('PG_USER'),
    "password": os.getenv('PG_PASSWORD'),
    "host": os.getenv('PG_DATABASE'),
    "port": os.getenv('PG_PORT'),
    "db": os.getenv('PG_DATABASE')
}

DATA_DIR = "/opt/airflow/data"

default_args = {
    "owner": "airflow",
    "retries": 2,
}

with DAG(
    dag_id="nyc_taxi_ingestion",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2021, 12, 31),
    schedule_interval="@monthly",
    catchup=True,
    max_active_runs=1,
    default_args=default_args,
) as dag:

    for taxi_type in ["green", "yellow"]:

        table_name = f"{taxi_type}_taxi_{{{{ execution_date.strftime('%Y_%m') }}}}"

        csv_gz = f"{DATA_DIR}/{taxi_type}_{{{{ execution_date.strftime('%Y_%m') }}}}.csv.gz"
        csv = f"{DATA_DIR}/{taxi_type}_{{{{ execution_date.strftime('%Y_%m') }}}}.csv"

        url = (
            "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/"
            f"{taxi_type}/{taxi_type}_tripdata_{{{{ execution_date.strftime('%Y-%m') }}}}.csv.gz"
        )

        download = PythonOperator(
            task_id=f"download_{taxi_type}",
            python_callable=download_and_unzip,
            op_kwargs={
                "url": url,
                "output_gz": csv_gz,
                "output_csv": csv,
            },
        )

        load = PythonOperator(
            task_id=f"load_{taxi_type}",
            python_callable=load_csv_to_postgres,
            op_kwargs={
                "csv_path": csv,
                "table_name": table_name,
                "taxi_type": taxi_type,
                **PG_CONFIG,
            },
        )

        download >> load
