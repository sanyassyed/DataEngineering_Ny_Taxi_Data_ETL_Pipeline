# Module 3 Homework: Data Warehousing & BigQuery

In this homework we'll practice working with BigQuery and Google Cloud Storage.

## Data

For this homework we will be using the Yellow Taxi Trip Records for January 2024 - June 2024 (not the entire year of data).

Parquet Files are available from the New York City Taxi Data found here:

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Loading the data

You can use the following scripts to load the data into your GCS bucket:

- Python script: [load_yellow_taxi_data.py](./load_yellow_taxi_data.py)
- Jupyter notebook with DLT: [DLT_upload_to_GCP.ipynb](./DLT_upload_to_GCP.ipynb)

You will need to generate a Service Account with GCS Admin privileges or be authenticated with the Google SDK, and update the bucket name in the script.

If you are using orchestration tools such as Kestra, Mage, Airflow, or Prefect, do not load the data into BigQuery using the orchestrator.

Make sure that all 6 files show in your GCS bucket before beginning.

Note: You will need to use the PARQUET option when creating an external table.


## BigQuery Setup

Create an external table using the Yellow Taxi Trip Records. 

```sql
CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.yellow_tripdata_2024_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://ny-taxi-yellow/yellow_tripdata_2024-*.parquet']
);
```

Create a (regular/materialized) table in BQ using the Yellow Taxi Trip Records (do not partition or cluster this table). 
```sql
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_2024` AS
SELECT * FROM `ny_taxi.yellow_tripdata_2024_external`;
```

## Question 1. Counting records

What is count of records for the 2024 Yellow Taxi Data?
- 20,332,093
```sql
SELECT COUNT(*) FROM `ny_taxi.yellow_tripdata_2024`;
```



## Question 2. Data read estimation

Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
 
What is the **estimated amount** of data that will be read when this query is executed on the External Table and the Table?

- 0 MB for the External Table and 155.12 MB for the Materialized Table

```sql
SELECT COUNT(DISTINCT PULocationIDs)
FROM `ny_taxi.yellow_tripdata_2024_external`;
```


## Question 3. Understanding columnar storage

Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table.

Why are the estimated number of Bytes different?
- BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires 
reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

```sql
SELECT PULocationIDs
FROM `ny_taxi.yellow_tripdata_2024`;
```

```sql
SELECT PULocationIDs, DOLocationID
FROM `ny_taxi.yellow_tripdata_2024`;
```

## Question 4. Counting zero fare trips

How many records have a fare_amount of 0?

- 8,333

```sql
SELECT COUNT(*)
FROM ny_taxi.yellow_tripdata_2024
WHERE fare_amount = 0;
```

## Question 5. Partitioning and clustering

What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

- Partition by tpep_dropoff_datetime and Cluster on VendorID

```sql
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_2024_par_clus`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `ny_taxi.yellow_tripdata_2024`;
```

## Question 6. Partition benefits

Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime
2024-03-01 and 2024-03-15 (inclusive)
```sql
SELECT DISTINCT VendorIDs
FROM `ny_taxi.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime >= '2024-03-01' AND 
      tpep_dropoff_datetime <= '2024-03-15';
```

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? 
```sql
SELECT DISTINCT VendorIDs
FROM `ny_taxi.yellow_tripdata_2024_par_clus`
WHERE tpep_dropoff_datetime >= '2024-03-01' AND 
      tpep_dropoff_datetime <= '2024-03-15';
```

Choose the answer which most closely matches.
 
- 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table


## Question 7. External table storage

Where is the data stored in the External Table you created?

- GCP Bucket

## Question 8. Clustering best practices

It is best practice in Big Query to always cluster your data:

- False


## Question 9. Understanding table scans

No Points: Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? Why?
```sql
SELECT COUNT(*)
FROM `ny_taxi.yellow_tripdata_2024`;
```
0 because BQ uses metadata to get this info.

## Submitting the solutions

Form for submitting: https://courses.datatalks.club/de-zoomcamp-2026/homework/hw3


## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and).

### Example post for LinkedIn

```
🚀 Week 3 of Data Engineering Zoomcamp by @DataTalksClub complete!

Just finished Module 3 - Data Warehousing with BigQuery. Learned how to:

✅ Create external tables from GCS bucket data
✅ Build materialized tables in BigQuery
✅ Partition and cluster tables for performance
✅ Understand columnar storage and query optimization
✅ Analyze NYC taxi data at scale

Working with 20M+ records and learning how partitioning reduces query costs!

Here's my homework solution: <LINK>

Following along with this amazing free course - who else is learning data engineering?

You can sign up here: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```

### Example post for Twitter/X

```
📊 Module 3 of Data Engineering Zoomcamp done!

- BigQuery & GCS
- External vs materialized tables
- Partitioning & clustering
- Query optimization

My solution: <LINK>

Free course by @DataTalksClub: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```