import polars as pl
from polars import DataFrame

def read_raw_csv(file_path: str) -> DataFrame:
    return pl.read_csv(file_path)