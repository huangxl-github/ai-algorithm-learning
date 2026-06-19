"""
W1 周四～周五练习：Python 基础语法
可被 verify_w1.py 自动检验。
"""


def describe_value(value) -> str:
    """返回变量类型名称字符串。"""
    return type(value).__name__


def classify_number(n: int) -> str:
    """根据数值返回分类：正数 / 零 / 负数。"""
    if n > 0:
        return "正数"
    if n == 0:
        return "零"
    return "负数"


def sum_range(start: int, end: int) -> int:
    """用 for 循环计算 [start, end] 闭区间整数之和。"""
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


def fizz_buzz(n: int) -> list[str]:
    """返回 1..n 的 FizzBuzz 结果列表（巩固 if/for）。"""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
