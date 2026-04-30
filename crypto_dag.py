from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append('/opt/airflow/dags')
from extract_data import get_binance_data, transform_data, load_data_to_postgres

default_args = {
    'owner': 'triet',
    'depends_on_past': False,
    'start_date': datetime(2026, 4, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'crypto_etl_pipeline',
    default_args=default_args,
    description='Tự động lấy dữ liệu BTC mỗi giờ',
    schedule_interval='@hourly', # Chạy mỗi tiếng một lần
    catchup=False
)

def run_etl():
    # Gọi lại đúng quy trình 3 bước bạn đã làm
    raw = get_binance_data(limit=10)
    if raw:
        clean = transform_data(raw)
        load_data_to_postgres(clean)

etl_task = PythonOperator(
    task_id='run_crypto_etl',
    python_callable=run_etl,
    dag=dag,
)