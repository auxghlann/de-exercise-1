import sys
from pathlib import Path
# Add project root to sys.path so 'pipeline' can be imported anywhere
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.decorators import task

import polars as pl

from pipeline import (
    read_raw_csv,
    transform_data,
    load_to_duckdb
)

with DAG(
    dag_id="job_application_data_pipeline",
    start_date=datetime(2026, 10, 4),
    schedule=None,
    catchup=False,
    tags=["data_pipeline", "job_application_data"]
) as dag:

    @task
    def run_extract_and_transform_data() -> str:
        csv_path = str(PROJECT_ROOT / "data" / "job_applications.csv")
        df_safe = transform_data(read_raw_csv(csv_path))

        governed_file_path = PROJECT_ROOT / "data"/ "governed" / "governed_data.parquet"
        governed_file_path.parent.mkdir(parents=True, exist_ok=True)

        df_safe.write_parquet(governed_file_path)

        return str(governed_file_path)
    
    @task
    def run_load_governed_data(file_path: str) -> None:
        db_path = str(PROJECT_ROOT / "data" / "warehouse.duckdb")
        load_to_duckdb(parquet_file_path=file_path, db_path=db_path)


    governed_file = run_extract_and_transform_data()
    run_load_governed_data(governed_file)








