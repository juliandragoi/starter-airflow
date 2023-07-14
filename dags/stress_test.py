from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator


dag = DAG('long_running', description='Long Running DAG',
          schedule_interval='0 */4 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

commands = BashOperator(
task_id='long_running_task'
,bash_command='sleep 5000'
,dag=dag
)