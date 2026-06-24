# W5 学习指南：Pandas 入门

> 本周目标：用 Pandas 读取、查看、清洗表格数据  
> 练习文件：`code/week05/practice.py`  
> 示例数据：`code/week05/data/titanic_dirty.csv`  
> 参考答案：`code/week05/pandas_core.py`  
> 检验：`python scripts/verify_week.py --week 5`

---

## 为什么学 Pandas？

NumPy 擅长**数值数组**；真实数据多是**带列名的表格**（CSV、Excel）。Pandas 的 **DataFrame** 就是「表格」，是数据分析的第一步。

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()      # 看前几行
df.info()      # 列类型、缺失值
df.describe()  # 数值列统计
```

---

## 学习顺序

| 顺序 | 主题 | 练习 |
|------|------|------|
| 1 | Series / DataFrame 创建 | 1～2 |
| 2 | 读取与概览 | 3～4 |
| 3 | 列选择、行过滤 | 5～6 |
| 4 | 缺失值处理 | 7～8 |
| 5 | 类型转换、去重 | 9 |
| 6 | 周六项目：数据清洗 | 10 |

---

## 一、Series 与 DataFrame

**Series**：一列数据（带索引）

```python
s = pd.Series([88, 92, 76], name="score")
# 0    88
# 1    92
# 2    76
```

**DataFrame**：多张 Series 组成的表

```python
df = pd.DataFrame({
    "name": ["张三", "李四"],
    "score": [88, 92],
})
```

---

## 二、读取与概览

```python
df = pd.read_csv("titanic_dirty.csv")

df.head(3)       # 前 3 行
df.shape         # (行数, 列数)
df.columns       # 列名列表
df.info()        # 非空数量、dtype
df.describe()    # 数值列：count/mean/std/min/max
```

---

## 三、列选择与行过滤

```python
df["Age"]                    # 选一列 → Series
df[["Name", "Age"]]          # 选多列 → DataFrame

df[df["Sex"] == "female"]    # 条件过滤
df[df["Age"] > 30]           # 数值条件
```

---

## 四、缺失值

```python
df.isna().sum()              # 每列缺失个数
df["Age"].fillna(0)          # 填 0（不推荐盲目填）
df["Age"].fillna(df["Age"].median())  # 用中位数填
df.dropna(subset=["Age"])    # 删掉 Age 为空的行
```

---

## 五、类型转换与去重

```python
pd.to_numeric(df["Age"], errors="coerce")  # 无效值变 NaN
df.drop_duplicates(subset=["Name"])        # 按姓名去重
```

`errors="coerce"`：遇到 `"invalid"` 这类无法转换的值 → 变成 `NaN`，而不是报错。

---

## 六、W5 周六项目：清洗泰坦尼克数据

对 `titanic_dirty.csv` 完成：

1. 读取 CSV  
2. `Age` 转数值（无效变 NaN），用**中位数**填充  
3. `Fare` 转数值，用**均值**填充  
4. 删除 `Name` 重复行（保留第一条）  
5. 返回清洗后的 DataFrame  

---

## 动手步骤

1. 确认 Pandas 已安装：`python -c "import pandas; print(pandas.__version__)"`
2. 打开 `code/week05/practice.py`，完成 `# TODO`
3. 运行 `python code/week05/practice.py`
4. 运行 `python scripts/verify_week.py --week 5`

---

## 自测题

1. Series 和 DataFrame 区别？  
2. `df["Age"]` 和 `df[["Age"]]` 返回类型有何不同？  
3. `fillna` 和 `dropna` 区别？  
4. `errors="coerce"` 做什么？  
5. 为什么清洗数据在 ML 之前很重要？

<details>
<summary>答案</summary>

1. Series 是一列；DataFrame 是多列表  
2. 前者 Series，后者 DataFrame（双括号）  
3. fillna 填充缺失；dropna 删除含缺失的行/列  
4. 转换失败时变成 NaN 而不是报错  
5. 脏数据会导致模型训练失败或结果不可靠

</details>
