Topic: Apache Airflow

Дата видачі: 14.12.2022

Дата здачі: 23.12.2022

Максимальна оцінка: 15 балів

Виконання - індивідуальне!

Результатом виконання завдання для перевірки буде посилання на гілку в gitlab репозиторії (залити посилання нижче Text reply - > Send your reply.). 

PM Academy Apache Airflow practice

Problem statement:

Create table order_status_stats with columns dt date, order_status_name varchar(100), orders_count int
Fill the table with orders count aggregated from sale table and grouped by date and order status name.
Acceptance criteria:

Table order_status_stats is created via docker compose or inside airflow DAG.
Table order_status_stats is filled with data with Airflow DAG.
Fork this repo to you private one.
Create MR to master branch with all required scripts and docs.
Tech tips:

You may use Airflow Postgres Operator.
Pay attention that database port for connection from Airflow should be 5432.
