-- Enrich and deduplicate trip data
-- Demonstrates enrichment and surrogate key generation
-- Note: Data quality analysis available in analyses/trips_data_quality.sql
{{ config(materialized='view') }}
with unioned as (
    select * from {{ ref('int_trips_unioned') }}
),

-- Deduplicate first to reduce the row count before hashing
deduplicated as (
    select * from unioned
    qualify row_number() over(
        partition by vendor_id, pickup_datetime, pickup_location_id, service_type
        order by dropoff_datetime
    ) = 1
),

payment_types as (
    select * from {{ ref('payment_type_lookup') }}
),

cleaned_and_enriched as (
    select
        -- Generate unique trip identifier (surrogate key pattern)
        {{ dbt_utils.generate_surrogate_key(['d.vendor_id', 'd.pickup_datetime', 'd.pickup_location_id', 'd.service_type']) }} as trip_id,

        -- Identifiers
        d.vendor_id,
        d.service_type,
        d.rate_code_id,

        -- Location IDs
        d.pickup_location_id,
        d.dropoff_location_id,

        -- Timestamps
        d.pickup_datetime,
        d.dropoff_datetime,

        -- Trip details
        d.store_and_fwd_flag,
        d.passenger_count,
        d.trip_distance,
        d.trip_type,

        -- Payment breakdown
        d.fare_amount,
        d.extra,
        d.mta_tax,
        d.tip_amount,
        d.tolls_amount,
        d.ehail_fee,
        d.improvement_surcharge,
        d.total_amount,
        d.payment_type,

        -- Enrich with payment type description
        coalesce(pt.description, 'Unknown') as payment_type_description
    from deduplicated d
    left join payment_types pt on coalesce(d.payment_type, 0) = pt.payment_type
)

select * from cleaned_and_enriched
