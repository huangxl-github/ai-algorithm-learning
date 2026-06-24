"""
W5 参考答案：Pandas 入门
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def create_score_series(scores: list[float]) -> pd.Series:
    return pd.Series(scores, name="score")


def create_student_dataframe(names: list[str], scores: list[float]) -> pd.DataFrame:
    return pd.DataFrame({"name": names, "score": scores})


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def get_basic_info(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "cols": len(df.columns),
        "columns": list(df.columns),
        "missing_total": int(df.isna().sum().sum()),
    }


def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return df[columns]


def filter_by_sex(df: pd.DataFrame, sex: str) -> pd.DataFrame:
    return df[df["Sex"] == sex]


def count_missing(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()


def fill_age_with_median(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["Age"] = pd.to_numeric(result["Age"], errors="coerce")
    result["Age"] = result["Age"].fillna(result["Age"].median())
    return result


def fill_fare_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["Fare"] = pd.to_numeric(result["Fare"], errors="coerce")
    result["Fare"] = result["Fare"].fillna(result["Fare"].mean())
    return result


def remove_duplicate_names(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["Name"], keep="first")


def clean_titanic_data(path: Path) -> pd.DataFrame:
    """W5 核心项目：完整清洗流程。"""
    df = load_csv(path)
    df = fill_age_with_median(df)
    df = fill_fare_with_mean(df)
    df = remove_duplicate_names(df)
    return df.reset_index(drop=True)
