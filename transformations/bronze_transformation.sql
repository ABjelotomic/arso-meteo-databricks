CREATE OR REFRESH STREAMING TABLE arso_obs_bronze
AS SELECT 
    *,
    _metadata.file_path AS source_file, 
    current_timestamp() AS ingested_at
FROM STREAM read_files(
    '/Volumes/weather/raw/arso_landing/xml',
    format => 'xml',
    rowTag => 'metData',
    inferColumnTypes => 'false'
);
