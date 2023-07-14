from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator


dag = DAG('high_frequency', description='high_frequency DAG',
          schedule_interval='*/5 * * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

commands = BashOperator(
task_id='high_frequency_task'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)