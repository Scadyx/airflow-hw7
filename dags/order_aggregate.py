from datetime import timedelta

from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from pendulum import yesterday

from helpers.default_args import default_args


with DAG(
        dag_id="order_aggregate",
        default_args=default_args,
        description="Homework_7",
        schedule_interval=timedelta(days=1),
        start_date=yesterday(),
        tags=["dummy"],
        catchup=False
) as dag:
    create_table = PostgresOperator(
        task_id="create_tables",
        postgres_conn_id="postgres_data",
        sql="data/create_tables.sql"
    )

    fill_agg = PostgresOperator(
        task_id="fill_agg",
        postgres_conn_id="postgres_data",
        sql="data/fill_agg_data.sql"
    )

create_table >> fill_agg
