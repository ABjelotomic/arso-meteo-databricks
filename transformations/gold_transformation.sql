{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "1b2fe454-dfc7-48fd-b28d-8e9a99c561ec",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "CREATE OR REFRESH MATERIALIZED VIEW weather.gold.arso_daily_station\n",
    "AS SELECT\n",
    "  station_id, station_name, to_date(from_utc_timestamp(obs_ts_utc, 'Europe/Ljubljana')) as obs_date,\n",
    "  count(t) AS n_obs, min(t) AS min_t, max(t) AS max_t, avg(t) AS avg_t\n",
    "FROM weather.silver.arso_obs_silver\n",
    "GROUP BY station_id, station_name, obs_date"
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
   "notebookName": "gold_transformation.sql",
   "widgets": {}
  },
  "language_info": {
   "name": "sql"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}