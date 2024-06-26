from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="example",
    schedule='@daily',
    start_date =datetime(2022,1,1),
    tags = ['stock_market'],
    catchup=False
)

def example():
    @task
    def extract():
        print("Extracting data from stock market")
        return 195.5
    
    @task
    def transform(value):
        print("Transforming data from stock market")
        print(value)
        return int(value * 1.1)
    
    @task
    def load(value):
        print("Loading data to stock market")
        print(value)
    
    load(transform(extract()))
    # extract() >> transform() >> load()

example()