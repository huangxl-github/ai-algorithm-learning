"""
W2 动手练习：请完成所有 # TODO 标记的函数。
运行：python code/week02/practice.py
检验：python scripts/verify_week.py --week 2

提示：卡住时可参考 code/week02/python_core.py（参考答案）
"""

from __future__ import annotations

import csv
from pathlib import Path


# ========== 练习 1～2：列表 ==========

def get_first_and_last(items: list) -> tuple:
    """返回列表的第一个和最后一个元素，格式 (first, last)。"""
    return (items[0], items[-1])


def list_slice_middle(items: list) -> list:
    """返回列表中间部分（去掉第一个和最后一个）。"""
    return items[1:-1]


# ========== 练习 3～4：字典 ==========

def build_student(name: str, age: int, score: float) -> dict:
    """用传入参数构建并返回一个字典：{"name": ..., "age": ..., "score": ...}"""
    return {
        "name": name,
        "age": age,
        "score": score
    }


def count_words(text: str) -> dict[str, int]:
    """统计每个单词出现次数。按空格分割，忽略大小写。"""
    # TODO: 你来写（提示：用 dict.get(word, 0) + 1）
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# ========== 练习 5～6：函数 ==========

def celsius_to_fahrenheit(c: float) -> float:
    """摄氏转华氏：F = C * 9/5 + 32"""
    # TODO: 你来写
    return c * 9/5 + 32


def average(numbers: list[float]) -> float:
    """返回列表平均值；空列表返回 0.0。"""
    # TODO: 你来写
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# ========== 练习 7：列表推导式 ==========

def filter_even(numbers: list[int]) -> list[int]:
    """用列表推导式返回所有偶数。"""
    # TODO: 你来写，格式 [n for n in numbers if ...]
    return [n for n in numbers if n % 2 == 0]


# ========== 练习 8～10：CSV（周六项目） ==========

def read_csv_column(csv_path: Path, column: str) -> list[str]:
    """读取 CSV 某一列的所有值（字符串列表）。"""
    # TODO: 你来写
    # 提示：csv.DictReader，循环 row，取 row[column]
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row[column] for row in reader]


def read_csv_numeric_stats(csv_path: Path, column: str) -> dict[str, float]:
    """
    W2 核心项目：读取 CSV 数值列，返回 {"mean": 均值, "max": 最大值, "count": 个数}。
    空数据时 mean/max/count 都为 0.0。
    """
    values: list[float] = []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = row.get(column, "").strip()
            if raw:
                values.append(float(raw))

    if not values:
        return {"mean": 0.0, "max": 0.0, "count": 0.0}

    return {
        "mean": sum(values) / len(values),
        "max": max(values),
        "count": float(len(values)),
    }


# ========== 自测运行（写完函数后取消下面注释来测试） ==========

def _run_self_test() -> None:
    """本地自测，方便你看到每个函数的结果。"""
    print("=== W2 练习自测 ===")

    assert get_first_and_last([10, 20, 30]) == (10, 30), "练习1失败"
    print("[OK] 练习1 get_first_and_last")

    assert list_slice_middle([1, 2, 3, 4, 5]) == [2, 3, 4], "练习2失败"
    print("[OK] 练习2 list_slice_middle")

    assert build_student("小明", 18, 90.0) == {"name": "小明", "age": 18, "score": 90.0}, "练习3失败"
    print("[OK] 练习3 build_student")

    assert count_words("Hello hello World") == {"hello": 2, "world": 1}, "练习4失败"
    print("[OK] 练习4 count_words")

    assert abs(celsius_to_fahrenheit(0) - 32.0) < 0.01, "练习5失败"
    print("[OK] 练习5 celsius_to_fahrenheit")

    assert average([10, 20, 30]) == 20.0, "练习6失败"
    assert average([]) == 0.0, "练习6空列表失败"
    print("[OK] 练习6 average")

    assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6], "练习7失败"
    print("[OK] 练习7 filter_even")

    data_file = Path(__file__).parent / "data" / "sample_scores.csv"
    cols = read_csv_column(data_file, "name")
    assert len(cols) == 5, "练习8失败"
    print(f"[OK] 练习8 read_csv_column → {cols}")

    stats = read_csv_numeric_stats(data_file, "score")
    assert stats["max"] == 95.0 and stats["count"] == 5.0, "练习9-10失败"
    print(f"[OK] 练习9-10 read_csv_numeric_stats → 均值={stats['mean']:.2f}, 最大={stats['max']}")

    print("\n全部练习通过！请运行: python scripts/verify_week.py --week 2")


if __name__ == "__main__":
    try:
        _run_self_test()
    except Exception as e:
        print(f"\n还有练习未完成或写错了: {e}")
        print("请继续完成 practice.py 中的 # TODO")
