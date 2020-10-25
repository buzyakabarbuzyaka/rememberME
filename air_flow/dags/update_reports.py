from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from uuid import uuid4
from pprint import pprint

dag = DAG('simple_print',
          schedule_interval=timedelta(seconds=45),
          start_date=datetime(2020, 10, 25, 0))


def print_context(**context):
    print("im alive")
    print(str(uuid4()))
    pprint(context)
    return 'Whatever you return gets printed in the logs'


run_this = PythonOperator(
    task_id='print_the_context',
    # task_id=str(uuid4()),
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)

# def workflow():
#     print("AM ALIVE!!!")
#     # print(context)
#
#
# PythonOperator(
#     task_id=str(uuid4()),
#     python_callable=workflow,
#     # provide_context=True,
#     dag=dag)
