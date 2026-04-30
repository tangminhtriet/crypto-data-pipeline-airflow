FROM apache/airflow:2.8.0
USER airflow
RUN pip install --no-cache-dir requests pandas sqlalchemy psycopg2-binary