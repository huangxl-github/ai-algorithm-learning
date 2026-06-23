# W4 学习指南：NumPy 入门

> 本周目标：掌握 NumPy 数组操作，为机器学习数学基础做准备  
> 练习文件：`code/week04/practice.py`  
> 参考答案：`code/week04/numpy_core.py`  
> 检验：`python scripts/verify_week.py --week 4`

---

## 为什么学 NumPy？

Python 普通列表做数值计算**慢**，代码也冗长。NumPy 提供** ndarray（多维数组）**，速度更快，也是 Pandas、PyTorch 的基础。

```python
import numpy as np

# 普通 list
[a + b for a, b in zip([1,2,3], [4,5,6])]  # [5, 7, 9]

# NumPy（更简洁、更快）
np.array([1,2,3]) + np.array([4,5,6])      # array([5, 7, 9])
```

---

## 学习顺序

| 顺序 | 主题 | 练习 |
|------|------|------|
| 1 | 数组创建、shape、dtype | 1～2 |
| 2 | 索引、切片、布尔索引 | 3～4 |
| 3 | 数组运算、广播 | 5～6 |
| 4 | 聚合函数 | 7 |
| 5 | 线性代数 + 周六项目 | 8～10 |

---

## 一、创建数组

```python
import numpy as np

a = np.array([1, 2, 3])           # 一维
b = np.array([[1, 2], [3, 4]])     # 二维
c = np.zeros((2, 3))               # 2行3列全0
d = np.ones((3, 3))                # 全1
e = np.arange(0, 10, 2)            # [0,2,4,6,8]
f = np.linspace(0, 1, 5)           # 0到1均匀分5个数

a.shape    # (3,) 形状
a.dtype    # int64  数据类型
```

---

## 二、索引与切片

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]       # 10
arr[-1]      # 50
arr[1:4]     # [20, 30, 40]

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrix[0, 1]     # 2（第1行第2列）
matrix[:, 0]     # [1, 4, 7]（所有行的第1列）
matrix[1, :]     # [4, 5, 6]（第2行）

# 布尔索引：选出大于3的元素
matrix[matrix > 3]   # [4, 5, 6, 7, 8, 9]
```

---

## 三、数组运算与广播

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b        # [11, 22, 33]
a * 2        # [2, 4, 6]
a ** 2       # [1, 4, 9]

# 广播：不同 shape 也能运算
arr = np.array([[1,2,3], [4,5,6]])
arr + 10     # 每个元素加10
```

---

## 四、聚合函数

```python
arr = np.array([1, 2, 3, 4, 5])

arr.sum()      # 15
arr.mean()     # 3.0
arr.max()      # 5
arr.min()      # 1
arr.argmax()   # 4（最大值的下标）
```

---

## 五、线性代数

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

a.T                    # 转置
np.dot(a, b)           # 矩阵乘法
a @ b                  # 同上（推荐写法）
np.linalg.norm(a)      # 范数
```

---

## 六、W4 周六项目：手写矩阵乘法

不用 `np.dot`，用循环实现：

```
C[i][j] = sum(A[i][k] * B[k][j])  对所有 k
```

输入两个 2D 数组，返回乘积矩阵。

---

## 动手步骤

1. 确认 NumPy 已安装：`python -c "import numpy; print(numpy.__version__)"`
2. 打开 `code/week04/practice.py`，完成 `# TODO`
3. 运行 `python code/week04/practice.py`
4. 运行 `python scripts/verify_week.py --week 4`

---

## 自测题

1. `np.array([1,2,3]).shape` 是什么？  
2. `arr[arr > 5]` 是什么操作？  
3. 广播（broadcasting）是什么？  
4. `np.dot` 和 `*` 有什么区别？  
5. 为什么 AI 领域几乎都用 NumPy？

<details>
<summary>答案</summary>

1. `(3,)`  
2. 布尔索引，选出大于5的元素  
3. 不同形状的数组按规则自动扩展后运算  
4. `*` 是逐元素乘，`np.dot` / `@` 是矩阵乘法  
5. 快、简洁，是科学计算标准库

</details>
