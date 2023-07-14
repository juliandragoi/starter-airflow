from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator


dag = DAG('high_concurrency', description='high_concurrency DAG',
          schedule_interval='0 */4 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

taskx = BashOperator(
task_id='taskx'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)


task1 = BashOperator(
task_id='task1'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task2 = BashOperator(
task_id='task2'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task3 = BashOperator(
task_id='task3'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task4 = BashOperator(
task_id='task4'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task5 = BashOperator(
task_id='task5'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task6 = BashOperator(
task_id='task6'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task7 = BashOperator(
task_id='task7'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task8 = BashOperator(
task_id='task8'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task9 = BashOperator(
task_id='task9'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task10 = BashOperator(
task_id='task10'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task11 = BashOperator(
task_id='task11'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task12 = BashOperator(
task_id='task12'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task13 = BashOperator(
task_id='task13'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)
task14 = BashOperator(
task_id='task14'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task15 = BashOperator(
task_id='task15'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task16 = BashOperator(
task_id='task16'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task17 = BashOperator(
task_id='task17'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task18 = BashOperator(
task_id='task18'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task19 = BashOperator(
task_id='task19'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task20 = BashOperator(
task_id='task20'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task21 = BashOperator(
task_id='task21'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task22 = BashOperator(
task_id='task22'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task23 = BashOperator(
task_id='task23'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task24 = BashOperator(
task_id='task24'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task25 = BashOperator(
task_id='task25'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task26 = BashOperator(
task_id='task26'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task27 = BashOperator(
task_id='task27'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task28 = BashOperator(
task_id='task28'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task29 = BashOperator(
task_id='task29'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task30 = BashOperator(
task_id='task30'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task31 = BashOperator(
task_id='task31'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task32 = BashOperator(
task_id='task32'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task33 = BashOperator(
task_id='task33'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task34 = BashOperator(
task_id='task34'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task35 = BashOperator(
task_id='task35'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task36 = BashOperator(
task_id='task36'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task37 = BashOperator(
task_id='task37'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task38 = BashOperator(
task_id='task38'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task39 = BashOperator(
task_id='task39'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task40 = BashOperator(
task_id='task40'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task41 = BashOperator(
task_id='task41'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task42 = BashOperator(
task_id='task42'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task43 = BashOperator(
task_id='task43'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task44 = BashOperator(
task_id='task44'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task45 = BashOperator(
task_id='task45'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task46 = BashOperator(
task_id='task46'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task47 = BashOperator(
task_id='task47'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task48 = BashOperator(
task_id='task48'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task49 = BashOperator(
task_id='task49'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task50 = BashOperator(
task_id='task50'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task51 = BashOperator(
task_id='task51'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task52 = BashOperator(
task_id='task52'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task53 = BashOperator(
task_id='task53'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)

task54 = BashOperator(
task_id='task54'
,bash_command='echo -----JD_TEST----- The time is: `date +"%Y-%m-%d %T"`'
,dag=dag
)
