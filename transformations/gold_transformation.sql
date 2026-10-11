CREATE OR REFRESH MATERIALIZED VIEW weather.gold.arso_daily_station
AS SELECT
  station_id, station_name, to_date(from_utc_timestamp(obs_ts_utc, 'Europe/Ljubljana')) as obs_date,
  count(t) AS n_obs, min(t) AS min_t, max(t) AS max_t, avg(t) AS avg_t
FROM weather.silver.arso_obs_silver
GROUP BY station_id, station_name, obs_date
