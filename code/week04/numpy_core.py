"""
W4 参考答案：NumPy 入门
"""

from __future__ import annotations

import numpy as np


def create_range_array(start: int, stop: int, step: int = 1) -> np.ndarray:
    return np.arange(start, stop, step)


def create_zeros_matrix(rows: int, cols: int) -> np.ndarray:
    return np.zeros((rows, cols))


def get_shape_and_dtype(arr: np.ndarray) -> tuple[tuple, str]:
    return arr.shape, str(arr.dtype)


def get_column(matrix: np.ndarray, col_index: int) -> np.ndarray:
    return matrix[:, col_index]


def get_row(matrix: np.ndarray, row_index: int) -> np.ndarray:
    return matrix[row_index, :]


def filter_greater_than(arr: np.ndarray, threshold: float) -> np.ndarray:
    return arr[arr > threshold]


def add_scalar(arr: np.ndarray, value: float) -> np.ndarray:
    return arr + value


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a * b


def array_stats(arr: np.ndarray) -> dict[str, float]:
    if arr.size == 0:
        return {"sum": 0.0, "mean": 0.0, "max": 0.0, "argmax": -1.0}
    return {
        "sum": float(arr.sum()),
        "mean": float(arr.mean()),
        "max": float(arr.max()),
        "argmax": float(arr.argmax()),
    }


def matrix_transpose(matrix: np.ndarray) -> np.ndarray:
    return matrix.T


def vector_norm(vec: np.ndarray) -> float:
    return float(np.linalg.norm(vec))


def matrix_multiply_manual(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """不用 np.dot，用三重循环实现矩阵乘法。"""
    rows_a, cols_a = a.shape
    rows_b, cols_b = b.shape
    if cols_a != rows_b:
        raise ValueError("矩阵形状不匹配，无法相乘")

    result = np.zeros((rows_a, cols_b))
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i, j] += a[i, k] * b[k, j]
    return result
