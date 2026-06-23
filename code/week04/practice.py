"""
W4 动手练习：NumPy 入门
运行：python code/week04/practice.py
检验：python scripts/verify_week.py --week 4
参考答案：code/week04/numpy_core.py
"""

from __future__ import annotations

import numpy as np


# ========== 练习 1～2：数组创建 ==========

def create_range_array(start: int, stop: int, step: int = 1) -> np.ndarray:
    """用 np.arange 创建等差数组，如 arange(0, 10, 2) → [0,2,4,6,8]"""
    # TODO
    pass


def create_zeros_matrix(rows: int, cols: int) -> np.ndarray:
    """创建 rows 行 cols 列的全零矩阵。"""
    # TODO: np.zeros((rows, cols))
    pass


def get_shape_and_dtype(arr: np.ndarray) -> tuple[tuple, str]:
    """返回 (shape, dtype字符串)，如 ((2, 3), 'float64')"""
    # TODO
    pass


# ========== 练习 3～4：索引与切片 ==========

def get_column(matrix: np.ndarray, col_index: int) -> np.ndarray:
    """取矩阵的某一列，如 matrix[:, col_index]"""
    # TODO
    pass


def get_row(matrix: np.ndarray, row_index: int) -> np.ndarray:
    """取矩阵的某一行，如 matrix[row_index, :]"""
    # TODO
    pass


def filter_greater_than(arr: np.ndarray, threshold: float) -> np.ndarray:
    """布尔索引：返回所有大于 threshold 的元素。"""
    # TODO: arr[arr > threshold]
    pass


# ========== 练习 5～6：数组运算 ==========

def add_scalar(arr: np.ndarray, value: float) -> np.ndarray:
    """每个元素加上 value（广播）。"""
    # TODO
    pass


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """两个数组逐元素相乘（不是矩阵乘法）。"""
    # TODO
    pass


# ========== 练习 7：聚合函数 ==========

def array_stats(arr: np.ndarray) -> dict[str, float]:
    """返回 sum, mean, max, argmax。空数组时 sum/mean/max=0, argmax=-1。"""
    # TODO
    pass


# ========== 练习 8～9：线性代数 ==========

def matrix_transpose(matrix: np.ndarray) -> np.ndarray:
    """矩阵转置。"""
    # TODO: matrix.T
    pass


def vector_norm(vec: np.ndarray) -> float:
    """向量范数（长度），使用 np.linalg.norm。"""
    # TODO
    pass


# ========== 练习 10：周六项目 ==========

def matrix_multiply_manual(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    不用 np.dot / @，用循环手写矩阵乘法。
    C[i,j] = sum(A[i,k] * B[k,j])
    形状不匹配时 raise ValueError。
    """
    # TODO
    pass


def _run_self_test() -> None:
    print("=== W4 练习自测 ===")

    arr = create_range_array(0, 10, 2)
    assert np.array_equal(arr, [0, 2, 4, 6, 8]), "练习1失败"
    print("[OK] 练习1 create_range_array")

    z = create_zeros_matrix(2, 3)
    assert z.shape == (2, 3) and z.sum() == 0, "练习2失败"
    print("[OK] 练习2 create_zeros_matrix")

    shape, dtype = get_shape_and_dtype(np.array([[1.0, 2.0], [3.0, 4.0]]))
    assert shape == (2, 2), "练习2 shape失败"
    print("[OK] 练习2 get_shape_and_dtype")

    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert np.array_equal(get_column(m, 0), [1, 4, 7]), "练习3失败"
    assert np.array_equal(get_row(m, 1), [4, 5, 6]), "练习4失败"
    assert np.array_equal(filter_greater_than(m, 5), [6, 7, 8, 9]), "练习4布尔索引失败"
    print("[OK] 练习3-4 索引切片")

    assert np.array_equal(add_scalar(np.array([1, 2, 3]), 10), [11, 12, 13]), "练习5失败"
    assert np.array_equal(elementwise_multiply(np.array([1, 2, 3]), np.array([4, 5, 6])), [4, 10, 18]), "练习6失败"
    print("[OK] 练习5-6 数组运算")

    stats = array_stats(np.array([1, 2, 3, 4, 5]))
    assert stats["sum"] == 15 and stats["mean"] == 3.0 and stats["argmax"] == 4, "练习7失败"
    print("[OK] 练习7 array_stats")

    a = np.array([[1, 2], [3, 4]])
    assert np.array_equal(matrix_transpose(a), [[1, 3], [2, 4]]), "练习8失败"
    assert abs(vector_norm(np.array([3.0, 4.0])) - 5.0) < 0.01, "练习9失败"
    print("[OK] 练习8-9 线性代数")

    b = np.array([[5, 6], [7, 8]])
    result = matrix_multiply_manual(a, b)
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected), "练习10失败"
    print("[OK] 练习10 matrix_multiply_manual")

    print("\n全部练习通过！请运行: python scripts/verify_week.py --week 4")


if __name__ == "__main__":
    try:
        _run_self_test()
    except Exception as e:
        print(f"\n还有练习未完成或写错了: {e}")
        print("请继续完成 practice.py 中的 # TODO")
