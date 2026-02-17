{{ config(materialized='table') }}
with fhv_data as (
    select * from {{ source('raw', 'fhv_tripdata') }}
),

filtered_data as (
    select
        -- identifiers
        cast(dispatching_base_num as string) as dispatching_base_num,
        cast(affiliated_base_number as string) as affiliated_base_number,

        -- timestamps
        cast(pickup_datetime as timestamp) as pickup_datetime,
        cast(dropoff_datetime as timestamp) as dropoff_datetime,

        -- trip info
        cast(pulocationid as integer) as pickup_location_id,
        cast(dolocationid as integer) as dropoff_location_id,
        cast(sr_flag as string) as sr_flag
    
    from fhv_data
    -- Filter out records with null dispatching_base_num (data quality requirement)
    where dispatching_base_num is NOT NULL
)

select * from filtered_data