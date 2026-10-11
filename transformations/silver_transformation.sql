CREATE OR REFRESH MATERIALIZED VIEW weather.silver.arso_obs_silver
(
  CONSTRAINT val_temp_range EXPECT (t BETWEEN -50 AND 50) ON VIOLATION DROP ROW
)
AS SELECT
  -- key
  domain_meteosiId                                        AS station_id,
  to_timestamp(tsValid_issued_RFC822, 'dd MMM yyyy HH:mm:ss Z') AS obs_ts_utc,

  -- station attributes
  domain_title                                            AS station_name,
  try_cast(nullif(domain_lat, '')      AS DOUBLE)         AS lat,
  try_cast(nullif(domain_lon, '')      AS DOUBLE)         AS lon,
  try_cast(nullif(domain_altitude, '') AS INT)            AS altitude_m,

  -- measures
  try_cast(nullif(t, '')         AS DOUBLE) AS t,
  try_cast(nullif(td, '')        AS DOUBLE) AS td,
  try_cast(nullif(rh, '')        AS DOUBLE) AS rh,
  try_cast(nullif(msl, '')       AS DOUBLE) AS msl,
  try_cast(nullif(ff_val, '')    AS DOUBLE) AS ff,
  try_cast(nullif(ffmax_val, '') AS DOUBLE) AS ff_max,
  try_cast(nullif(dd_val, '')    AS DOUBLE) AS dd,
  try_cast(nullif(rr_val, '')    AS DOUBLE) AS rr,
  try_cast(nullif(gSunRad, '')   AS DOUBLE) AS g_sun_rad,
  try_cast(nullif(snow, '')      AS DOUBLE) AS snow,
  try_cast(nullif(vis_val, '')   AS DOUBLE) AS vis,

  -- lineage
  source_file,
  ingested_at
FROM weather.bronze.arso_obs_bronze
QUALIFY row_number() OVER (PARTITION BY station_id, obs_ts_utc ORDER BY ingested_at DESC) = 1;
