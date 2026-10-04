from pathlib import Path
import duckdb

def load_to_duckdb(parquet_file_path: str, db_path:str) -> None:
    """
        Ingests a parquet file directly into a DuckDB table
    """
    
    # Ensure parent folder exist
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    with duckdb.connect(db_path) as conn:

        ## Create table using parquet schema only
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS job_application_tracker_sanitized AS
            SELECT * FROM read_parquet('{parquet_file_path}')
            WHERE 1=0
        """)

        # Append new records
        conn.execute(f"""
            INSERT INTO job_application_tracker_sanitized
            SELECT * FROM read_parquet('{parquet_file_path}')
        """)






## -----------------
##    Deprecated
## -----------------
# DB_CONNECTION = "postgresql://postgres:postgres@localhost:5432/postgres"
# ENGINE = create_engine(DB_CONNECTION)

# def load_to_db(df_transformed: DataFrame) -> None:
#     df_transformed.write_database(
#         table_name="job_application_tracker_sanitized",
#         connection=ENGINE,
#         if_table_exists="append",
#         engine='sqlalchemy'
#     )


