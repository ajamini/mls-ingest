# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
#
# def test_function():
#     print("hello world python")
#
# my_dag = DAG(
#     'simple_python_dag',
#     start_date=datetime(2023, 2, 1),
#     schedule_interval='@daily'
# )
#
# python_task = PythonOperator(
#     task_id='python_task',
#     python_callable=test_function,
#     dag=my_dag
# )