# Extend from the Apache Airflow image
FROM apache/airflow:2.6.3
USER root
RUN sudo mkdir -p /opt/retsmanager
ENV PYTHONPATH=PYTHONPATH:/opt/retsmanager

USER airflow
ADD requirements.txt /tmp
RUN pip install psycopg2-binary
RUN pip install -r /tmp/requirements.txt

