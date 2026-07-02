from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Définition du DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='hello_etl',
    schedule='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    def extract():
        print("Step 1 : Data extraction")

    def transform():
        print("Step 2 : Data transformation")

    def load():
        print("Step 3 : Data loading")

    t1 = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id='load_task',
        python_callable=load
    )