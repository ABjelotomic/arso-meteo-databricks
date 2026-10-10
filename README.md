Readme · MD
# arso-meteo-databricks
 
Study project for the **Databricks Certified Data Engineer Associate** exam. Instead of tutorial data, all hands-on work is done on Slovenian weather observations from ARSO (Slovenian Environment Agency), built up as a small lakehouse on Databricks Free Edition.
 
## Goal
 
Practise every exam domain on one realistic project:
 
- Platform and Delta Lake basics
- Data ingestion (COPY INTO, Auto Loader)
- Transformation and modeling (medallion layers, Lakeflow Spark Declarative Pipelines)
- Lakeflow Jobs
- Governance and security (Unity Catalog, row filters, column masks)
- CI/CD (Git folders, Declarative Automation Bundles)
- Troubleshooting and optimization
## Data source
 
ARSO automatic stations, latest snapshot XML (one `<metData>` element per station, refreshed roughly every 30 minutes):
 
`https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml`
 
> TODO: verify ARSO terms of use and add proper attribution before sharing this repo publicly.
 
## Architecture
 
| Layer | Object | Description |
|---|---|---|
| Landing | UC volume `weather.raw.arso_landing` | Timestamped raw XML files |
| Bronze | `weather.bronze.arso_obs_bronze` | Raw rows plus file metadata, ingested with Auto Loader |
| Silver | materialized view | Typed columns, UTC timestamps, deduplicated per station and observation time |
| Gold | `weather.gold.arso_daily_station` | Daily aggregates per station |
 
The silver and gold layers are defined in a Lakeflow Spark Declarative Pipeline (`arso_pipeline`).
 
## Repository layout
 
> Update this section as the repo grows.
 
```
.
├── README.md
├── notebooks/      # ingestion, transformation and governance exercises
├── pipelines/      # Lakeflow pipeline source
└── databricks.yml  # bundle definition (added during the CI/CD phase)
```
 
## Environment
 
- Databricks Free Edition (serverless compute, Unity Catalog)
- Databricks CLI for bundle commands
- Git folders in the workspace linked to this repo

