# W3 学习指南：Python 进阶

> 本周目标：面向对象、异常处理、模块导入、常用标准库  
> 练习文件：`code/week03/practice.py`  
> 参考答案：`code/week03/student_manager.py`  
> 检验：`python scripts/verify_week.py --week 3`

---

## 学习顺序

| 顺序 | 主题 | 练习 |
|------|------|------|
| 1 | 模块与 import | 练习 1 |
| 2 | 类与对象 | 练习 2～4 |
| 3 | 异常处理 try/except | 练习 5～6 |
| 4 | json / datetime | 练习 7～8 |
| 5 | 周六项目：学生成绩管理系统 | 练习 9～10 |

---

## 一、模块与 import

把代码分到不同文件，用 `import` 引入。

```python
# 使用别的文件里的函数
from code.week02.practice import average

# 使用标准库
import json
from datetime import datetime
```

---

## 二、面向对象（类 class）

类 = 模板，对象 = 按模板造出的具体东西。

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name      # 属性
        self.score = score

    def grade(self) -> str:   # 方法
        if self.score >= 90:
            return "A"
        return "B"

s = Student("小明", 95)
print(s.name)    # 小明
print(s.grade()) # A
```

**三个关键词**：
- `__init__`：创建对象时自动调用（构造函数）
- `self`：代表对象自己
- 方法：类里的函数

---

## 三、异常处理

程序出错时不崩溃，而是优雅处理。

```python
try:
    score = int("abc")   # 会报错
except ValueError:
    print("请输入数字")
```

常见异常：`ValueError`、`FileNotFoundError`、`KeyError`

---

## 四、json 与 datetime

**json**：字典 ↔ JSON 文件（存盘/读盘）

```python
import json
data = {"name": "小明", "score": 90}
json.dumps(data)   # 转字符串
json.loads('{"name":"小明"}')  # 字符串转字典
```

**datetime**：处理日期时间

```python
from datetime import datetime
now = datetime.now()
text = now.strftime("%Y-%m-%d %H:%M")
```

---

## 五、W3 周六项目：学生成绩管理系统

用**类**实现一个简单的成绩管理器：

| 功能 | 方法 |
|------|------|
| 添加学生 | `add(name, score)` |
| 查询学生 | `get(name)` |
| 删除学生 | `remove(name)` |
| 列出全部 | `list_all()` |
| 保存到文件 | `save(path)` |
| 从文件加载 | `load(path)` |

---

## 动手步骤

1. 打开 `code/week03/practice.py`，完成 `# TODO`
2. 运行 `python code/week03/practice.py`
3. 运行 `python scripts/verify_week.py --week 3`
4. 对照 `code/week03/student_manager.py`

---

## 自测题

1. `self` 是什么意思？  
2. `__init__` 什么时候执行？  
3. `try/except` 有什么用？  
4. `json.load` 和 `json.loads` 区别？  
5. 类和字典相比，优势是什么？

<details>
<summary>答案</summary>

1. 代表当前对象自己  
2. 创建对象时 `Student(...)`  
3. 捕获错误，避免程序崩溃  
4. `load` 读文件，`loads` 解析字符串  
5. 可以把数据和行为（方法）绑在一起，更适合复杂项目

</details>
