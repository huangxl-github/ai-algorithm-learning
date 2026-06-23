"""
W3 动手练习：Python 进阶（面向对象 + 异常 + json）
运行：python code/week03/practice.py
检验：python scripts/verify_week.py --week 3
参考答案：code/week03/student_manager.py
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

# ========== 练习 1：模块意识 ==========
def average(numbers: list[float]) -> float:
    """返回列表平均值；空列表返回 0.0。"""
    # TODO: 你来写
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def use_average_from_week2() -> float:
    """从 W2 的 practice 模块导入 average 函数，计算 [10,20,30] 的平均值。"""
    # TODO: from code.week02.practice import average
    # 注意：如果 import 报错，可用相对导入或直接写 return 20.0 先理解概念
    return average([10,20,30])


# ========== 练习 2～4：类与对象 ==========

class Student:
    """学生类：name, score 两个属性，grade() 返回等级。"""

    def __init__(self, name: str, score: float) -> None:
        # TODO: 保存 name 和 score 到 self
        self.name = name
        self.score = score

    def grade(self) -> str:
        """90+ A, 80+ B, 60+ C, 否则 D"""
        # TODO: 你来写
        if self.score >= 90:
            return "A"
        if self.score >= 80:
            return "B"
        if self.score >= 60:
            return "C"
        return "D"

    def __str__(self) -> str:
        # TODO: 返回如 "小明: 90分(A)"
        return f"{self.name}: {self.score}分({self.grade()})"


class StudentManager:
    """学生成绩管理器。"""

    def __init__(self) -> None:
        # TODO: 用字典存储学生，key=姓名, value=Student 对象
        self._students: dict[str, Student] = {}

    def add(self, name: str, score: float) -> None:
        """添加学生。姓名不能为空，分数 0～100。"""
        # TODO: 校验 + 存入字典
        if not name.strip():
            raise ValueError("姓名不能为空")
        if not 0 <= score <= 100:
            raise ValueError("分数必须在 0～100 之间")
        self._students[name] = Student(name=name, score=score)

    def get(self, name: str) -> Student | None:
        # TODO
        return self._students.get(name)

    def remove(self, name: str) -> bool:
        """删除学生，成功返回 True，不存在返回 False。"""
        # TODO
        if name in self._students:
            del self._students[name]
            return True
        return False

    def list_all(self) -> list[Student]:
        """返回所有学生，按姓名排序。"""
        # TODO: sorted(..., key=lambda s: s.name)
        return sorted(self._students.values(), key=lambda s: s.name)

    def count(self) -> int:
        # TODO
        return len(self._students)


# ========== 练习 5～6：异常处理 ==========

def safe_int(value: str, default: int = 0) -> int:
    """安全转整数，失败返回 default。"""
    # TODO: try/except ValueError
    try:
        return int(value)
    except ValueError:
        return default


def safe_divide(a: float, b: float) -> float | None:
    """相除，除数为 0 时返回 None 而不是报错。"""
    # TODO: try/except ZeroDivisionError
    try:
        return a / b
    except ZeroDivisionError:
        return None


# ========== 练习 7～8：json 与 datetime ==========

def student_to_json(student: Student) -> str:
    """把 Student 对象转成 JSON 字符串。"""
    # TODO: json.dumps({"name": ..., "score": ..., "grade": ...}, ensure_ascii=False)
    return json.dumps({"name": student.name, "score": student.score, "grade": student.grade()}, ensure_ascii=False)


def current_date_string() -> str:
    """返回当前日期字符串，格式 YYYY-MM-DD。"""
    # TODO: datetime.now().strftime("%Y-%m-%d")
    return datetime.now().strftime("%Y-%m-%d")


# ========== 练习 9～10：文件存取（周六项目） ==========

def save_students(manager: StudentManager, path: Path) -> None:
    """把管理器中学生保存到 JSON 文件。"""
    # TODO: 构建字典列表，json.dumps 写入文件
    payload = {
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "students": [{"name": student.name, "score": student.score, "grade": student.grade()} for student in manager.list_all()],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_students(path: Path) -> StudentManager:
    """从 JSON 文件加载学生到新的 StudentManager。"""
    # TODO: 读取文件，json.loads，循环 add
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    manager = StudentManager()
    for student in data.get("students", []):
        manager.add(student["name"], student["score"])
    return manager


def _run_self_test() -> None:
    print("=== W3 练习自测 ===")

    assert use_average_from_week2() == 20.0, "练习1失败"
    print("[OK] 练习1")

    s = Student("小明", 95)
    assert s.grade() == "A", "练习2-4 grade失败"
    assert "小明" in str(s), "练习2-4 __str__失败"
    print("[OK] 练习2-4 Student")

    mgr = StudentManager()
    mgr.add("张三", 88)
    mgr.add("李四", 72)
    assert mgr.count() == 2
    assert mgr.get("张三").score == 88
    assert mgr.remove("王五") is False
    assert mgr.remove("李四") is True
    assert mgr.count() == 1
    print("[OK] 练习2-4 StudentManager")

    assert safe_int("42") == 42
    assert safe_int("abc", 0) == 0
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(1, 0) is None
    print("[OK] 练习5-6 异常处理")

    assert "小明" in student_to_json(Student("小明", 90))
    assert len(current_date_string()) == 10
    print("[OK] 练习7-8 json/datetime")

    data_file = Path(__file__).parent / "data" / "students.json"
    save_students(mgr, data_file)
    loaded = load_students(data_file)
    assert loaded.count() == 1
    assert loaded.get("张三").score == 88
    print("[OK] 练习9-10 文件存取")

    print("\n全部练习通过！请运行: python scripts/verify_week.py --week 3")


if __name__ == "__main__":
    try:
        _run_self_test()
    except Exception as e:
        print(f"\n还有练习未完成或写错了: {e}")
        print("请继续完成 practice.py 中的 # TODO")
