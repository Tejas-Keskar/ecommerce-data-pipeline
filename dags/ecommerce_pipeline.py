from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Define variables
WATCH_FOLDER = "<Path to the folder in which data will be available>"
HDFS_PATH = "<Path to the hdfs folder to save data>"
SPARK_SCRIPT = "<Path to the data processing spark file>"

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

# Define DAG
with DAG(
    dag_id='ecommerce_data_pipeline',
    default_args=default_args,
    schedule_interval='@weekly',
    catchup=False
) as dag:
    
    # Sensor to detect new files
    wait_for_file = FileSensor(
        task_id='wait_for_file',
        filepath=WATCH_FOLDER,
        poke_interval=60,
        timeout=600,
        mode='poke'
    )
    
    # Move file to HDFS
    move_to_hdfs = BashOperator(
        task_id='move_to_hdfs',
        bash_command=f'hdfs dfs -moveFromLocal {WATCH_FOLDER}/* {HDFS_PATH}'
    )
    
    # Run Spark job
    run_spark_job = SparkSubmitOperator(
        task_id='run_spark_job',
        application=SPARK_SCRIPT,
        conn_id='spark_default',
        verbose=True
    )

    # Delete processed files from local machine
    delete_local_files = BashOperator(
        task_id='delete_local_files',
        bash_command=f'rm -rf {WATCH_FOLDER}/*'
    )
    
    # Task dependencies
    wait_for_file >> move_to_hdfs >> run_spark_job >> delete_local_files
