from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello Airflow world!")

with DAG(
    dag_id="hello_world",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["beginner"]
) as dag:

    task = PythonOperator(
        task_id="say_hello",
        python_callable=hello_world
    )