import math
import time
from datetime import timedelta
from random import random

from rq import Queue
from airflow import DAG
from airflow.models import TaskInstance
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, task
from datetime import datetime

from airflow.operators.subdag import SubDagOperator
from redis.client import Redis

from scripts.ingest_properties import ingest_properties, fetch_properties, ingest_image

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'start_date': datetime(2023, 8, 4)
}

queue = Queue(name='property_ingest', connection=Redis(host='retsmanager_redis_1'))

def fetch_properties_and_add_to_queue():
    fetch_properties()


def add_data_to_database():
    # result = ingest_properties()
    rand = math.ceil(random() * 100)
    print("sleeping for %s" % rand)
    time.sleep(rand)

    return [{'MLS': 'asdfasdf', 'random': random()}]


def ingest_image(*op_args, ti: TaskInstance):
    listings = ti.xcom_pull(task_ids=op_args[0])
    print(listings)
    # ingest_image(listings)


with DAG('property_dag_v3', default_args=default_args, schedule_interval=timedelta(hours=1), catchup=False) as dag:

    fetch_properties_task = PythonOperator(
        task_id='fetch_properties',
        python_callable=fetch_properties_and_add_to_queue,
    )

    # subtasks2 = []
    for i in range(0, 5):
        add_data = PythonOperator(
                task_id='add_database_%s' % i,
                python_callable=add_data_to_database
            )

        subtasks = []
        for j in range(0, 5):
            subtasks.append(PythonOperator(
                    task_id='ingest_image_%s_%s' % (i,j),
                    python_callable=add_data_to_database
                ))

        chain(fetch_properties_task, *[add_data], *[subtasks])

        #     chain(fetch_properties_task, *[
        #     PythonOperator(
        #         task_id='add_database_%s' % i,
        #         python_callable=add_data_to_database
        #     )])
        #
        # for j in range(0, 10):
        #     chain(add_data, *[
        #         PythonOperator(
        #             task_id='ingest_image_%s' % j,
        #             python_callable=add_data_to_database
        #         )])

        # j = 0
        #
        # add_data = chain(fetch_properties_task, *[
        #     chain(PythonOperator(
        #         task_id='add_database_%s' % i,
        #         python_callable=add_data_to_database
        #     ), *[
        #         PythonOperator(
        #             task_id='ingest_image_%s_%s' % (i, j + 1),
        #             python_callable=ingest_image,
        #             op_args=['add_database_%s' % i, j + 1]
        #         ),
        #         PythonOperator(
        #             task_id='ingest_image_%s_%s' % (i, j +2),
        #             python_callable=ingest_image,
        #             op_args=['add_database_%s' % i, j + 2]
        #         )
        #     ])
        # ])


