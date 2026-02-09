import pandas as pd
import psycopg2
import io


GREEN_SCHEMA = """
CREATE TABLE IF NOT EXISTS {table_name} (
    VendorID TEXT,
    lpep_pickup_datetime TIMESTAMP,
    lpep_dropoff_datetime TIMESTAMP,
    store_and_fwd_flag TEXT,
    RatecodeID TEXT,
    PULocationID TEXT,
    DOLocationID TEXT,
    passenger_count REAL,
    trip_distance REAL,
    fare_amount REAL,
    extra REAL,
    mta_tax REAL,
    tip_amount REAL,
    tolls_amount REAL,
    ehail_fee REAL,
    improvement_surcharge REAL,
    total_amount REAL,
    payment_type REAL,
    trip_type REAL,
    congestion_surcharge REAL
);
"""

YELLOW_SCHEMA = """
CREATE TABLE IF NOT EXISTS {table_name} (
    VendorID TEXT,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count REAL,
    trip_distance REAL,
    RatecodeID TEXT,
    store_and_fwd_flag TEXT,
    PULocationID TEXT,
    DOLocationID TEXT,
    payment_type REAL,
    fare_amount REAL,
    extra REAL,
    mta_tax REAL,
    tip_amount REAL,
    tolls_amount REAL,
    improvement_surcharge REAL,
    total_amount REAL,
    congestion_surcharge REAL
);
"""


def load_csv_to_postgres(
    csv_path,
    table_name,
    taxi_type,
    user,
    password,
    host,
    port,
    db
):
    conn = psycopg2.connect(
        user=user, password=password, host=host, port=port, dbname=db
    )
    cur = conn.cursor()

    schema_sql = GREEN_SCHEMA if taxi_type == "green" else YELLOW_SCHEMA
    cur.execute(schema_sql.format(table_name=table_name))
    conn.commit()

    for chunk in pd.read_csv(csv_path, chunksize=300_000):
        if taxi_type == "green":
            chunk["lpep_pickup_datetime"] = pd.to_datetime(chunk["lpep_pickup_datetime"])
            chunk["lpep_dropoff_datetime"] = pd.to_datetime(chunk["lpep_dropoff_datetime"])
        else:
            chunk["tpep_pickup_datetime"] = pd.to_datetime(chunk["tpep_pickup_datetime"])
            chunk["tpep_dropoff_datetime"] = pd.to_datetime(chunk["tpep_dropoff_datetime"])

        buffer = io.StringIO()
        chunk.to_csv(buffer, index=False, header=False)
        buffer.seek(0)

        cur.copy_expert(
            f"COPY {table_name} FROM STDIN WITH CSV NULL ''",
            buffer
        )
        conn.commit()

    cur.close()
    conn.close()
