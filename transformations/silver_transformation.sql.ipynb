{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "89c483c5-3ff8-4339-a28c-4b8fac5ea8ac",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "CREATE OR REFRESH MATERIALIZED VIEW weather.silver.arso_obs_silver\n",
    "(\n",
    "  CONSTRAINT val_temp_range EXPECT (t BETWEEN -50 AND 50) ON VIOLATION DROP ROW\n",
    ")\n",
    "AS SELECT\n",
    "  -- key\n",
    "  domain_meteosiId                                        AS station_id,\n",
    "  to_timestamp(tsValid_issued_RFC822, 'dd MMM yyyy HH:mm:ss Z') AS obs_ts_utc,\n",
    "\n",
    "  -- station attributes\n",
    "  domain_title                                            AS station_name,\n",
    "  try_cast(nullif(domain_lat, '')      AS DOUBLE)         AS lat,\n",
    "  try_cast(nullif(domain_lon, '')      AS DOUBLE)         AS lon,\n",
    "  try_cast(nullif(domain_altitude, '') AS INT)            AS altitude_m,\n",
    "\n",
    "  -- measures\n",
    "  try_cast(nullif(t, '')         AS DOUBLE) AS t,\n",
    "  try_cast(nullif(td, '')        AS DOUBLE) AS td,\n",
    "  try_cast(nullif(rh, '')        AS DOUBLE) AS rh,\n",
    "  try_cast(nullif(msl, '')       AS DOUBLE) AS msl,\n",
    "  try_cast(nullif(ff_val, '')    AS DOUBLE) AS ff,\n",
    "  try_cast(nullif(ffmax_val, '') AS DOUBLE) AS ff_max,\n",
    "  try_cast(nullif(dd_val, '')    AS DOUBLE) AS dd,\n",
    "  try_cast(nullif(rr_val, '')    AS DOUBLE) AS rr,\n",
    "  try_cast(nullif(gSunRad, '')   AS DOUBLE) AS g_sun_rad,\n",
    "  try_cast(nullif(snow, '')      AS DOUBLE) AS snow,\n",
    "  try_cast(nullif(vis_val, '')   AS DOUBLE) AS vis,\n",
    "\n",
    "  -- lineage\n",
    "  source_file,\n",
    "  ingested_at\n",
    "FROM weather.bronze.arso_obs_bronze\n",
    "QUALIFY row_number() OVER (PARTITION BY station_id, obs_ts_utc ORDER BY ingested_at DESC) = 1;\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "6"
   },
   "inputWidgetPreferences": null,
   "language": "sql",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "silver_transformation.sql",
   "widgets": {}
  },
  "language_info": {
   "name": "sql"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}