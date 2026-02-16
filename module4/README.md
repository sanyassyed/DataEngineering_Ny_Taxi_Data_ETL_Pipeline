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
uckdb ./taxi_rides_ny.duckdb 
.tables # to view the tables
.database # to view the database
SHOW ALL TABLES; # to view the tables and the database name and schema name
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
dbt seed
dbt run
dbt compile
dbt docs genrate
dbt docs serve
```
