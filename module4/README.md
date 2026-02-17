# Notes
* This part uses python3 installed as follows:
```bash
# Update package index
sudo apt update -y

# Upgrade existing packages
sudo apt upgrade -y

# -----------------------------
# Install basic system packages
# -----------------------------
sudo apt install -y python3-pip 
sudo apt install python3.12-venv
which python3
```

* Create virtual env for other packages
```bash
python3 -m venv .venv
# activate virtual env
source .venv/bin/activate
```

* Install duckdb - instructions [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/setup/local_setup.md)
```bash
# install dbt with duckdb plug
pip install dbt-duckdb
# install duckdb
sudo snap install duckdb
```
* initialize dbt
```bash
dbt init taxi_rides_ny
# Select option 1 for duckdb
```

* copy code to `ingest.py`
* Run the py script `python3 ./ingest.py`
* View data in duckdb after transfer `duckdb -ui`

* Alternate way to interact with duckdb in command line
```bash
cd /home/ubuntu/DataEngineering_Ny_Taxi_Data_ETL_Pipeline/module4/taxi_rides_ny
duckdb ./taxi_rides_ny.duckdb 
.tables # to view the tables
.database # to view the database
SHOW ALL TABLES; # to view the tables and the database name and schema name
# to see all schemas
SELECT * FROM duckdb_schemas();
.exit # to quit
```
* EDA
    * prod.yellow_tripdata rows:  109047518 
    * prod.green_tripdata rows: 7778101 

* Run dbt [ref](https://github.com/sanyassyed/DataEngineering_Retail_ETL_Pipeline/blob/main/docs/project_creation.md)
```bash
cd /home/ubuntu/DataEngineering_Ny_Taxi_Data_ETL_Pipeline/module4/taxi_rides_ny
dbt debug 
dbt deps

# Option 1
dbt build

# Option 2
dbt seed
dbt run

# Other commands for dbt GUI
dbt compile
dbt docs genrate
dbt docs serve
```
## Homework
```bash
dbt seed --target prod
dbt build --select stg_yellow_tripdata --target prod
dbt build --select stg_green_tripdata --target prod
dbt build --select int_trips_unioned --target prod
dbt run --select int_trips --target # prod dbt run --select int_trips --target prod
# if build fails use dbt retry

dbt run --select dim_zones --target prod

dbt run --select fct_trips --target prod
dbt run --select dim_vendors --target prod
dbt run --select fct_monthly_zone_revenue --target prod
```
```sql
-- Q3
SELECT COUNT(*) FROM prod.fct_monthly_zone_revenue;

--Q4
SELECT pickup_zone,
       SUM(revenue_monthly_total_amount) total
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green' AND
      YEAR(revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY SUM(revenue_monthly_total_amount) DESC;

-- Q5
SELECT SUM(total_monthly_trips) total_trips
FROM prod.fct_monthly_zone_revenue
WHERE trim(lower(service_type)) = 'green' AND
YEAR(revenue_month) = 2019 AND
MONTH(revenue_month) = 10;


--Q6
python3 ingest_fhv.py
SELECT COUNT(*) FROM prod.stg_fhv_tripdata WHERE YEAR(pickup_datetime) = 2019
```
