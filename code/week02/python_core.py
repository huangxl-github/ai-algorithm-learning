"""
W2 练习：Python 核心语法
可被 verify_week.py 自动检验。
"""

from __future__ import annotations

import csv
from pathlib import Path


def list_stats(numbers: list[int]) -> dict[str, int | float]:
    """返回列表的长度、最小值、最大值、平均值。"""
    if not numbers:
        return {"count": 0, "min": 0, "max": 0, "mean": 0.0}
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
    }


def word_count(text: str) -> dict[str, int]:
    """统计每个单词出现次数（简单按空格分割，转小写）。"""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def filter_even(numbers: list[int]) -> list[int]:
    """列表推导式：返回所有偶数。"""
    return [n for n in numbers if n % 2 == 0]


class Student:
    """简单学生类，用于练习面向对象前的函数+字典结构。"""

    def __init__(self, name: str, score: float) -> None:
        self.name = name
        self.score = score

    def grade(self) -> str:
        if self.score >= 90:
            return "A"
        if self.score >= 80:
            return "B"
        if self.score >= 60:
            return "C"
        return "D"


def read_csv_numeric_stats(csv_path: Path, column: str) -> dict[str, float]:
    """
    W2 周六项目核心：读取 CSV，统计指定数值列的均值和最大值。
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
