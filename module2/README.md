# Resources:
* [Airflow Implemented by an Alumn in 2025](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/blob/main/2_Workflow-Orchestration-AirFlow/airflow/dags/data_ingestion_local_optimized.py)
    * docker compose script inspired from here

## Steps to run Airflow
```bash
cd DataEngineering_Ny_Taxi_Data_ETL_Pipeline/module2/airflow

# check and modify the permissions for airflow to access the folders dags, logs and plugins
sudo chown -R 50000:0 logs dags plugins
sudo chmod -R 775 logs dags plugins

ls -ld logs dags plugins

docker compose up

# Goto localhost:8080 
#user & pwd same : airflow

# Start the docker compose for postgres db
cd /home/ubuntu/DataEngineering_Ny_Taxi_Data_ETL_Pipeline/module2/local_db
docker compose up -d

# to view the contents of postgres db use the following command
docker exec -it <container_id> psql -U root -d ny_taxi

```