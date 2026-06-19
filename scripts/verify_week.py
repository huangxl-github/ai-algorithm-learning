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

    return passed, total


WEEK_VERIFIERS = {
    1: verify_week1,
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
