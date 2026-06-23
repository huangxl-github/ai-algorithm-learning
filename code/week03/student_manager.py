"""
W3 参考答案：学生成绩管理系统（面向对象）
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Student:
    name: str
    score: float

    def grade(self) -> str:
        if self.score >= 90:
            return "A"
        if self.score >= 80:
            return "B"
        if self.score >= 60:
            return "C"
        return "D"


class StudentManager:
    """学生成绩管理器：增删查 + 文件存取。"""

    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def add(self, name: str, score: float) -> None:
        if not name.strip():
            raise ValueError("姓名不能为空")
        if not 0 <= score <= 100:
            raise ValueError("分数必须在 0～100 之间")
        self._students[name] = Student(name=name, score=score)

    def get(self, name: str) -> Student | None:
        return self._students.get(name)

    def remove(self, name: str) -> bool:
        if name in self._students:
            del self._students[name]
            return True
        return False

    def list_all(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda s: s.name)

    def count(self) -> int:
        return len(self._students)

    def save(self, path: Path) -> None:
        payload = {
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "students": [asdict(s) for s in self.list_all()],
        }
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self, path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        self._students.clear()
        for item in data.get("students", []):
            self.add(item["name"], float(item["score"]))


def safe_int(value: str, default: int = 0) -> int:
    """安全地把字符串转整数，失败时返回 default。"""
    try:
        return int(value)
    except ValueError:
        return default
