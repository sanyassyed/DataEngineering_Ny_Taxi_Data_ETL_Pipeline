# Instructions:
## Aim
The aim of the module is as follows
1. Create docker compose with pgdatabase and pgadmin
1. Create dockerfile with script to download data (yellow taxi 2021-01, green taxi 2025-11 & zones data) for ny taxi and load into pg database `ny_taxi`

## Steps to run the pipeline
* Run the pipeline as follows
```bash
docker-compose up
docker build -t taxi_ingest:v001 .

# check the network link:
docker network ls

# it's pipeline_default (or similar based on directory name)
# now run the script:
docker run -it --rm\
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
```

* Stop the containers
```bash
docker-compose down
```
