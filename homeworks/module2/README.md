# Module 2 Homework

## Questions

1) Within the execution for `Yellow` Taxi data for the year `2020` and month `12`: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?
- 128.3 MiB 


2) What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?
- `green_tripdata_2020-04.csv` 


3) How many rows are there for the `Yellow` Taxi data for all CSV files in the year 2020?

- 24,648,499 

**Query**
```sql
SELECT COUNT(*) AS total_rows
FROM (
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_01_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_02_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_03_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_04_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_05_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_06_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_07_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_08_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_09_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_10_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_11_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.yellow_tripdata_2020_12_ext`
);
```

4) How many rows are there for the `Green` Taxi data for all CSV files in the year 2020?
- 1,734,051 


**Query**
```sql
SELECT COUNT(*) AS total_rows
FROM (
  SELECT * FROM `zoomcamp.green_tripdata_2020_01_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_02_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_03_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_04_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_05_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_06_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_07_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_08_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_09_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_10_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_11_ext`
  UNION ALL
  SELECT * FROM `zoomcamp.green_tripdata_2020_12_ext`
);
```


5) How many rows are there for the `Yellow` Taxi data for the March 2021 CSV file?
- 1,925,152 


**Query**
```sql
SELECT COUNT(*) AS total_rows
FROM `zoomcamp.yellow_tripdata_2021_03_ext`;
```

6) How would you configure the timezone to New York in a Schedule trigger?
- Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration 

```yaml
triggers:
  - id: green_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *"
    timezone: America/New_York
    inputs:
      taxi: green
```

## Code:
All the code can be found in [this repository](../../module2/)
