FROM apache/airflow:2.8.1
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         wget \
         gzip \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
# to add the packages required by data_local_ingest.py
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir \
    apache-airflow-providers-postgres==5.7.1


