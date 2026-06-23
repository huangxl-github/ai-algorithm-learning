# W2 学习指南：Python 核心语法

> 本周目标：掌握列表、字典、函数、列表推导式、CSV 读写  
> 练习文件：`code/week02/practice.py`（你来写）  
> 参考答案：`code/week02/python_core.py`（写完后再对照）  
> 检验命令：`python scripts/verify_week.py --week 2`

---

## 学习顺序（建议 3～5 天，不必严格按天）

| 顺序 | 主题 | 对应练习 | 预计时间 |
|------|------|----------|----------|
| 1 | 列表 list | `practice.py` 练习 1～2 | 1～2 小时 |
| 2 | 字典 dict | `practice.py` 练习 3～4 | 1～2 小时 |
| 3 | 函数 | `practice.py` 练习 5～6 | 1～2 小时 |
| 4 | 列表推导式 | `practice.py` 练习 7 | 1 小时 |
| 5 | CSV 读写 | `practice.py` 练习 8～10 | 2～3 小时 |

---

## 一、列表 list

列表像一排带编号的盒子，可以装多个数据。

```python
scores = [88, 92, 76, 95, 81]

len(scores)      # 长度 → 5
scores[0]        # 第一个 → 88（下标从 0 开始）
scores[-1]       # 最后一个 → 81
scores[1:3]      # 切片 → [92, 76]

scores.append(99)    # 末尾添加
scores.insert(0, 60)  # 在位置 0 插入
scores.remove(76)     # 删除值为 76 的元素
```

**你要会**：创建列表、取值、切片、`append`、`len`、`sum`、`min`、`max`。

---

## 二、字典 dict

字典像一本「键 → 值」的对照表。

```python
student = {"name": "张三", "age": 25, "score": 88}

student["name"]           # 取值 → 张三
student.get("city", "未知")  # 没有 key 时返回默认值
student["city"] = "北京"   # 新增或修改

for key, value in student.items():
    print(key, value)
```

**常用技巧**：`dict.get(key, 0)` 统计词频时很好用。

---

## 三、函数

把重复代码打包成函数，方便复用。

```python
def add(a: int, b: int) -> int:
    """两个数相加。"""
    return a + b

result = add(3, 5)  # 8
```

**参数类型标注**（W1 学过）：
- `a: int` → 参数应该是整数
- `-> int` → 返回值是整数
- `-> None` → 没有返回值

---

## 四、列表推导式

用一行代码从列表生成新列表。

```python
numbers = [1, 2, 3, 4, 5, 6]

# 普通写法
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# 列表推导式（更简洁）
evens = [n for n in numbers if n % 2 == 0]
# 结果：[2, 4, 6]
```

---

## 五、CSV 文件读写

CSV 是逗号分隔的表格文件，数据分析里非常常见。

你的示例数据 `code/week02/data/sample_scores.csv`：

```csv
name,age,score,city
张三,25,88,北京
李四,30,92,上海
...
```

读取方式：

```python
import csv
from pathlib import Path

path = Path("code/week02/data/sample_scores.csv")
with path.open(encoding="utf-8") as f:
    reader = csv.DictReader(f)   # 按列名读取，每行是一个字典
    for row in reader:
        print(row["name"], row["score"])
```

**W2 周六项目**：读取 `score` 列，算出**平均值**和**最大值**。

---

## 六、动手步骤（今天就开始）

### 第 1 步：打开练习文件

打开 `code/week02/practice.py`，找到 `# TODO`，按提示填写代码。

### 第 2 步：运行自检

```powershell
cd d:\cursor_study\人工智能算法学习
python code/week02/practice.py
```

### 第 3 步：通过周检验

```powershell
python scripts/verify_week.py --week 2
```

### 第 4 步：对照答案（可选）

全部做完或卡住时，再看 `code/week02/python_core.py`。

### 第 5 步：打勾

在 `学习进度清单.md` 和 `progress/当前进度.md` 里勾选完成项。

---

## 七、10 道自测题（纸上或心里回答）

1. `[1,2,3][1]` 的结果是什么？  
2. `{"a": 1}.get("b", 0)` 的结果是什么？  
3. `len([10, 20, 30])` 是多少？  
4. `[x*2 for x in [1,2,3]]` 的结果是什么？  
5. 函数里 `return` 和不写 `return` 有什么区别？  
6. CSV 第一行通常是什么？  
7. `csv.DictReader` 每行返回什么类型？  
8. 列表 `append` 和 `insert(0, x)` 有什么区别？  
9. 如何判断一个数是偶数？  
10. `sum([1,2,3,4,5])` 等于多少？

<details>
<summary>点击查看答案</summary>

1. `2`  
2. `0`  
3. `3`  
4. `[2, 4, 6]`  
5. 不写 return 返回 `None`  
6. 表头（列名）  
7. 字典 `dict`  
8. append 加在末尾，insert(0) 加在开头  
9. `n % 2 == 0`  
10. `15`

</details>

---

## 八、本周交付物

- [ ] 完成 `practice.py` 全部练习
- [ ] `verify_week.py --week 2` 检验通过
- [ ] 能独立解释 `read_csv_numeric_stats` 每一行在做什么

完成后进入 **W3：Python 进阶（面向对象）**。
