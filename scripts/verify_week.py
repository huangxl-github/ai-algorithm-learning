#!/usr/bin/env python3
"""
学习进度自动检验脚本。
用法：
  python scripts/verify_week.py          # 检验当前进度所在周
  python scripts/verify_week.py --week 1 # 检验指定周
"""

from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ok(msg: str) -> None:
    print(f"  [通过] {msg}")


def fail(msg: str) -> None:
    print(f"  [未通过] {msg}")


def check_command(name: str, args: list[str] | None = None) -> bool:
    exe = shutil.which(name)
    if not exe:
        fail(f"未找到 {name}，请先安装")
        return False
    if args:
        result = subprocess.run([exe, *args], capture_output=True, text=True)
        if result.returncode != 0:
            fail(f"{name} {' '.join(args)} 执行失败")
            return False
        ok(f"{name} {' '.join(args)} → {result.stdout.strip() or 'OK'}")
    else:
        ok(f"已安装 {name} → {exe}")
    return True


def load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载模块: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_week1() -> tuple[int, int]:
    """返回 (通过数, 总项数)。"""
    passed = 0
    total = 0

    print("\n=== W1 环境检验 ===")
    checks = [
        ("python", ["--version"]),
        ("git", ["--version"]),
    ]
    for cmd, args in checks:
        total += 1
        if check_command(cmd, args):
            passed += 1

    for pkg, import_name in [("numpy", "numpy"), ("jupyter", "jupyter_core")]:
        total += 1
        try:
            __import__(import_name)
            ok(f"Python 包 {pkg} 已安装")
            passed += 1
        except ImportError:
            fail(f"Python 包 {pkg} 未安装 → 运行: pip install -r requirements.txt")

    guess_file = ROOT / "code" / "week01" / "guess_number.py"
    basics_file = ROOT / "code" / "week01" / "python_basics.py"

    total += 1
    if guess_file.exists():
        ok(f"W1 项目文件存在: {guess_file.relative_to(ROOT)}")
        passed += 1
    else:
        fail(f"缺少 W1 项目: {guess_file.relative_to(ROOT)}")

    print("\n=== W1 代码检验 ===")
    total += 1
    if basics_file.exists():
        mod = load_module(basics_file, "python_basics")
        tests = [
            (mod.describe_value(42), "int"),
            (mod.classify_number(-1), "负数"),
            (mod.sum_range(1, 5), 15),
            (mod.fizz_buzz(5), ["1", "2", "Fizz", "4", "Buzz"]),
        ]
        all_pass = all(actual == expected for actual, expected in tests)
        if all_pass:
            ok("python_basics.py 全部单元检验通过")
            passed += 1
        else:
            fail("python_basics.py 检验失败，请检查函数实现")
    else:
        fail(f"缺少练习文件: {basics_file.relative_to(ROOT)}")

    notes = ROOT / "notes" / "week01-环境配置笔记.md"
    total += 1
    if notes.exists() and notes.stat().st_size > 100:
        ok("环境配置笔记已创建")
        passed += 1
    else:
        fail("请完善 notes/week01-环境配置笔记.md（记录你的环境信息）")

    print("\n=== W1 GitHub 检验 ===")
    total += 1
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0 and "origin/main" in result.stdout:
        ok("本地 main 已关联 origin/main")
        passed += 1
    else:
        fail("请完成 git push -u origin main")

    return passed, total


def verify_week2() -> tuple[int, int]:
    """返回 (通过数, 总项数)。"""
    passed = 0
    total = 0

    practice_file = ROOT / "code" / "week02" / "practice.py"
    guide_file = ROOT / "notes" / "week02-学习指南.md"
    csv_file = ROOT / "code" / "week02" / "data" / "sample_scores.csv"

    print("\n=== W2 文件检验 ===")
    for path in [practice_file, guide_file, csv_file]:
        total += 1
        if path.exists():
            ok(f"文件存在: {path.relative_to(ROOT)}")
            passed += 1
        else:
            fail(f"缺少文件: {path.relative_to(ROOT)}")

    print("\n=== W2 练习检验（practice.py）===")
    total += 1
    if not practice_file.exists():
        fail("缺少 practice.py")
        return passed, total

    try:
        mod = load_module(practice_file, "practice_w2")
    except Exception as e:
        fail(f"无法加载 practice.py: {e}")
        return passed, total

    try:
        assert mod.get_first_and_last([10, 20, 30]) == (10, 30)
        assert mod.list_slice_middle([1, 2, 3, 4, 5]) == [2, 3, 4]
        assert mod.build_student("小明", 18, 90.0) == {"name": "小明", "age": 18, "score": 90.0}
        assert mod.count_words("Hello hello World") == {"hello": 2, "world": 1}
        assert abs(mod.celsius_to_fahrenheit(0) - 32.0) < 0.01
        assert mod.average([10, 20, 30]) == 20.0
        assert mod.average([]) == 0.0
        assert mod.filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        cols = mod.read_csv_column(csv_file, "name")
        assert len(cols) == 5
        stats = mod.read_csv_numeric_stats(csv_file, "score")
        assert stats["max"] == 95.0 and stats["count"] == 5.0
        assert abs(stats["mean"] - 86.4) < 0.01
        ok("practice.py 全部 10 项练习通过")
        ok(f"CSV score 列均值 = {stats['mean']:.2f}")
        passed += 1
    except Exception as e:
        fail(f"practice.py 练习未通过: {e}")
        fail("请打开 code/week02/practice.py 完成 # TODO 后重试")

    return passed, total


def verify_week3() -> tuple[int, int]:
    """返回 (通过数, 总项数)。"""
    passed = 0
    total = 0

    practice_file = ROOT / "code" / "week03" / "practice.py"
    guide_file = ROOT / "notes" / "week03-学习指南.md"

    print("\n=== W3 文件检验 ===")
    for path in [practice_file, guide_file]:
        total += 1
        if path.exists():
            ok(f"文件存在: {path.relative_to(ROOT)}")
            passed += 1
        else:
            fail(f"缺少文件: {path.relative_to(ROOT)}")

    print("\n=== W3 练习检验（practice.py）===")
    total += 1
    if not practice_file.exists():
        fail("缺少 practice.py")
        return passed, total

    try:
        mod = load_module(practice_file, "practice_w3")
        assert mod.use_average_from_week2() == 20.0
        s = mod.Student("小明", 95)
        assert s.grade() == "A"
        mgr = mod.StudentManager()
        mgr.add("张三", 88)
        mgr.add("李四", 72)
        assert mgr.count() == 2
        assert mgr.remove("王五") is False
        assert mod.safe_int("abc", 0) == 0
        assert mod.safe_divide(1, 0) is None
        assert "小明" in mod.student_to_json(mod.Student("小明", 90))
        data_file = ROOT / "code" / "week03" / "data" / "students.json"
        mod.save_students(mgr, data_file)
        loaded = mod.load_students(data_file)
        assert loaded.count() == 2
        ok("practice.py 全部 W3 练习通过")
        passed += 1
    except Exception as e:
        fail(f"practice.py 练习未通过: {e}")
        fail("请打开 code/week03/practice.py 完成 # TODO 后重试")

    return passed, total


def verify_week4() -> tuple[int, int]:
    """返回 (通过数, 总项数)。"""
    passed = 0
    total = 0

    practice_file = ROOT / "code" / "week04" / "practice.py"
    guide_file = ROOT / "notes" / "week04-学习指南.md"

    print("\n=== W4 文件检验 ===")
    for path in [practice_file, guide_file]:
        total += 1
        if path.exists():
            ok(f"文件存在: {path.relative_to(ROOT)}")
            passed += 1
        else:
            fail(f"缺少文件: {path.relative_to(ROOT)}")

    total += 1
    try:
        import numpy as np  # noqa: F401
        ok("NumPy 已安装")
        passed += 1
    except ImportError:
        fail("NumPy 未安装 → pip install numpy")

    print("\n=== W4 练习检验（practice.py）===")
    total += 1
    if not practice_file.exists():
        fail("缺少 practice.py")
        return passed, total

    try:
        import numpy as np
        mod = load_module(practice_file, "practice_w4")

        assert np.array_equal(mod.create_range_array(0, 10, 2), [0, 2, 4, 6, 8])
        z = mod.create_zeros_matrix(2, 3)
        assert z.shape == (2, 3)
        m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert np.array_equal(mod.get_column(m, 0), [1, 4, 7])
        assert np.array_equal(mod.filter_greater_than(m, 5), [6, 7, 8, 9])
        stats = mod.array_stats(np.array([1, 2, 3, 4, 5]))
        assert stats["mean"] == 3.0 and stats["argmax"] == 4
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        result = mod.matrix_multiply_manual(a, b)
        assert np.array_equal(result, [[19, 22], [43, 50]])
        ok("practice.py 全部 W4 练习通过")
        passed += 1
    except Exception as e:
        fail(f"practice.py 练习未通过: {e}")
        fail("请打开 code/week04/practice.py 完成 # TODO 后重试")

    return passed, total


def verify_week5() -> tuple[int, int]:
    """返回 (通过数, 总项数)。"""
    passed = 0
    total = 0

    practice_file = ROOT / "code" / "week05" / "practice.py"
    guide_file = ROOT / "notes" / "week05-学习指南.md"
    data_file = ROOT / "code" / "week05" / "data" / "titanic_dirty.csv"

    print("\n=== W5 文件检验 ===")
    for path in [practice_file, guide_file, data_file]:
        total += 1
        if path.exists():
            ok(f"文件存在: {path.relative_to(ROOT)}")
            passed += 1
        else:
            fail(f"缺少文件: {path.relative_to(ROOT)}")

    total += 1
    try:
        import pandas as pd  # noqa: F401
        ok("Pandas 已安装")
        passed += 1
    except ImportError:
        fail("Pandas 未安装 → pip install pandas")

    print("\n=== W5 练习检验（practice.py）===")
    total += 1
    if not practice_file.exists():
        fail("缺少 practice.py")
        return passed, total

    try:
        mod = load_module(practice_file, "practice_w5")
        cleaned = mod.clean_titanic_data(data_file)
        assert len(cleaned) == 9
        assert cleaned["Age"].isna().sum() == 0
        assert cleaned["Fare"].isna().sum() == 0
        females = mod.filter_by_sex(mod.load_csv(data_file), "female")
        assert len(females) == 5
        ok("practice.py 全部 W5 练习通过")
        ok(f"清洗后 {len(cleaned)} 行，Age/Fare 无缺失")
        passed += 1
    except Exception as e:
        fail(f"practice.py 练习未通过: {e}")
        fail("请打开 code/week05/practice.py 完成 # TODO 后重试")

    return passed, total


WEEK_VERIFIERS = {
    1: verify_week1,
    2: verify_week2,
    3: verify_week3,
    4: verify_week4,
    5: verify_week5,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="学习进度检验")
    parser.add_argument("--week", type=int, default=1, help="要检验的周次")
    args = parser.parse_args()

    verifier = WEEK_VERIFIERS.get(args.week)
    if verifier is None:
        print(f"第 {args.week} 周暂无自动检验，请对照 学习进度清单.md 手动打勾。")
        return 0

    passed, total = verifier()
    print(f"\n--- 结果: {passed}/{total} 项通过 ---")
    if passed == total:
        print("本周自动检验全部通过！请在 学习进度清单.md 中打勾。")
        return 0
    print("仍有未完成项，请补做后重新运行检验。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
