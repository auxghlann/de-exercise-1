import polars as pl
from polars import DataFrame

def __remove_sensitive_and_unusable_cols(df_raw: DataFrame) -> DataFrame:
    COLS_TO_REMOVE: list[str] = ["applicant_name", "email", "recruiter","notes"]
    df_safe = df_raw.drop(COLS_TO_REMOVE)
    
    return df_safe

def transform_data(df_raw: DataFrame) -> DataFrame:
    return __remove_sensitive_and_unusable_cols(df_raw)