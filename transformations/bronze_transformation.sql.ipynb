{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "5c96ef2e-db48-4b89-a1b8-23675427b27b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "CREATE OR REFRESH STREAMING TABLE arso_obs_bronze\n",
    "AS SELECT \n",
    "    *,\n",
    "    _metadata.file_path AS source_file, \n",
    "    current_timestamp() AS ingested_at\n",
    "FROM STREAM read_files(\n",
    "    '/Volumes/weather/raw/arso_landing/xml',\n",
    "    format => 'xml',\n",
    "    rowTag => 'metData',\n",
    "    inferColumnTypes => 'false'\n",
    ");"
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
   "notebookName": "bronze_transformation.sql",
   "widgets": {}
  },
  "language_info": {
   "name": "sql"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}