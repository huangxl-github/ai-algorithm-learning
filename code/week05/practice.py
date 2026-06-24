"""
W5 动手练习：Pandas 入门
运行：python code/week05/practice.py
检验：python scripts/verify_week.py --week 5
参考答案：code/week05/pandas_core.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


# ========== 练习 1～2：Series / DataFrame ==========

def create_score_series(scores: list[float]) -> pd.Series:
    """创建名为 score 的 Series。"""
    # TODO: pd.Series(scores, name="score")
    pass


def create_student_dataframe(names: list[str], scores: list[float]) -> pd.DataFrame:
    """创建含 name、score 两列的 DataFrame。"""
    # TODO
    pass


# ========== 练习 3～4：读取与概览 ==========

def load_csv(path: Path) -> pd.DataFrame:
    """读取 CSV 文件。"""
    # TODO: pd.read_csv(path)
    pass


def get_basic_info(df: pd.DataFrame) -> dict:
    """返回 rows, cols, columns, missing_total（缺失值总数）。"""
    # TODO
    pass


# ========== 练习 5～6：选择与过滤 ==========

def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """选取多列。"""
    # TODO: df[columns]
    pass


def filter_by_sex(df: pd.DataFrame, sex: str) -> pd.DataFrame:
    """筛选 Sex 列等于指定值的行。"""
    # TODO: df[df["Sex"] == sex]
    pass


# ========== 练习 7～8：缺失值 ==========

def count_missing(df: pd.DataFrame) -> pd.Series:
    """返回每列缺失值个数。"""
    # TODO: df.isna().sum()
    pass


def fill_age_with_median(df: pd.DataFrame) -> pd.DataFrame:
    """Age 转数值（errors='coerce'），用中位数填充缺失。"""
    # TODO: 先 copy，再 to_numeric，再 fillna(median)
    pass


# ========== 练习 9：去重 ==========

def remove_duplicate_names(df: pd.DataFrame) -> pd.DataFrame:
    """按 Name 列去重，保留第一条。"""
    # TODO: drop_duplicates(subset=["Name"], keep="first")
    pass


# ========== 练习 10：周六项目 ==========

def clean_titanic_data(path: Path) -> pd.DataFrame:
    """
    完整清洗 titanic_dirty.csv：
    1. 读取
    2. Age 中位数填充
    3. Fare 均值填充（需先 to_numeric）
    4. Name 去重
    5. reset_index(drop=True)
    """
    # TODO: 组合上面函数，或逐步写
    pass


def _run_self_test() -> None:
    print("=== W5 练习自测 ===")

    s = create_score_series([88, 92, 76])
    assert list(s) == [88, 92, 76] and s.name == "score", "练习1失败"
    print("[OK] 练习1 create_score_series")

    df0 = create_student_dataframe(["张三", "李四"], [88, 92])
    assert list(df0.columns) == ["name", "score"], "练习2失败"
    print("[OK] 练习2 create_student_dataframe")

    data_file = Path(__file__).parent / "data" / "titanic_dirty.csv"
    raw = load_csv(data_file)
    assert len(raw) == 10, "练习3失败"
    info = get_basic_info(raw)
    assert info["rows"] == 10 and info["missing_total"] >= 3, "练习4失败"
    print(f"[OK] 练习3-4 读取与概览 → 缺失值共 {info['missing_total']} 个")

    cols = select_columns(raw, ["Name", "Age", "Sex"])
    assert list(cols.columns) == ["Name", "Age", "Sex"], "练习5失败"
    females = filter_by_sex(raw, "female")
    assert len(females) == 5, "练习6失败"
    print("[OK] 练习5-6 选择与过滤")

    missing = count_missing(raw)
    assert missing["Age"] >= 2, "练习7失败"
    filled_age = fill_age_with_median(raw)
    assert filled_age["Age"].isna().sum() == 0, "练习8失败"
    print("[OK] 练习7-8 缺失值处理")

    deduped = remove_duplicate_names(raw)
    assert len(deduped) == 9, "练习9失败"
    print("[OK] 练习9 去重")

    cleaned = clean_titanic_data(data_file)
    assert len(cleaned) == 9, "练习10行数失败"
    assert cleaned["Age"].isna().sum() == 0, "练习10 Age仍有缺失"
    assert cleaned["Fare"].isna().sum() == 0, "练习10 Fare仍有缺失"
    print(f"[OK] 练习10 clean_titanic_data → {len(cleaned)} 行，Age/Fare 无缺失")

    print("\n全部练习通过！请运行: python scripts/verify_week.py --week 5")


if __name__ == "__main__":
    try:
        _run_self_test()
    except Exception as e:
        print(f"\n还有练习未完成或写错了: {e}")
        print("请继续完成 practice.py 中的 # TODO")
