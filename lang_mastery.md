# Python Language Mastery 

### 1. Variables, Types & Assignment

Python is dynamically typed—no need to declare types, but you can use type hints for clarity (especially important in large codebases).

```python
x = 42              # Integer
name = "Alice"      # String (str)
pi = 3.14           # Float
flag = True         # Boolean
nothing = None      # Null value
a, b, c = 1, 2, 3   # Multiple assignment (unpacking)
```
**Type hints** make code clearer and help with tools like linters and IDEs:
```python
def add(x: int, y: int) -> int:
    return x + y
```

---

### 2. Control Flow

#### If/Else
```python
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")
```
#### Loops
- **For** loops are used to iterate over sequences (lists, strings, etc.),
- **While** loops repeat as long as a condition is true.

```python
for i in range(3):
    print(i)  # 0, 1, 2

while x > 0:
    x -= 1
```
**Loop `else`:** Executes if the loop didn't break.
```python
for item in items:
    if item == target:
        break
else:
    print("Not found")
```

---

### 3. Functions & Arguments

Python functions can have:
- Positional/default arguments,
- Variable-length args (`*args` for tuple, `**kwargs` for dict).

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

def add(*args):   # Accepts any number of positional arguments
    return sum(args)

def config(**kwargs):  # Accepts any number of keyword arguments
    print(kwargs)
```

**Lambda functions** are small, anonymous functions:
```python
double = lambda x: x * 2
```

**Decorators** modify function behavior (useful for logging, timing, authentication, etc.):
```python
def logger(fn):
    def wrapper(*a, **k):
        print(f"Calling {fn.__name__}")
        return fn(*a, **k)
    return wrapper

@logger
def foo(): pass
```

---

### 4. Built-in Data Structures

#### Lists (dynamic arrays)
- Mutable, ordered, allow duplicates.
```python
nums = [1, 2, 3]
nums.append(4)
nums[0]   # 1 (indexing)
nums[1:3] # [2,3] (slicing)
nums.sort()
```

#### Dictionaries (hash maps)
- Key-value pairs, fast lookup, keys must be hashable.
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d.get('d', 0)     # Returns 0 instead of error if 'd' not found
for k, v in d.items():
    print(k, v)
```

#### Sets
- Unordered, unique elements, fast membership test.
```python
s = set([1, 2, 3])
s.add(4)
s1 | s2   # Union
s1 & s2   # Intersection
```

#### Tuples & NamedTuples
- Immutable sequences. NamedTuples give fields names (clarity).
```python
t = (1, 2, 3)
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, 2)
```

#### Collections
- Specialized containers for advanced use-cases.
```python
from collections import defaultdict, Counter, deque

dd = defaultdict(list)   # auto-initializes new keys to empty list
c = Counter([1,2,2,3])   # frequency count
q = deque([1,2,3])       # fast append/pop from both ends
```

---

### 5. Comprehensions & Generators

**Comprehensions**: concise way to build lists/sets/dicts.
```python
squares = [x*x for x in range(10)]
even = {x for x in range(10) if x%2 == 0}
doubled = {x: x*2 for x in range(5)}
```

**Generators**: produce items one at a time, saving memory.
```python
def gen():
    for i in range(10):
        yield i

g = (x*x for x in range(10))  # generator expression
```

---

### 6. String Handling

Strings are immutable, but have many built-in methods:
```python
s = " backend "
s.strip()         # "backend" (removes whitespace)
s.upper()         # " BACKEND "
s.lower()         # " backend "
s.replace("e", "E")
",".join(["a", "b"])   # "a,b"
s.split("e")      # splits on "e"
s.startswith("b")
s.endswith("d")
```

---

### 7. File I/O

Always use `with` to manage files (auto-closes on exit).
```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("file.txt", "w") as f:
    f.write("Hello\n")
```

---

### 8. Exception Handling

Handle errors gracefully.
```python
try:
    risky()
except ValueError as e:
    print(e)
except Exception as e:    # Catch-all
    print(e)
else:
    print("No error")
finally:
    print("Always runs")
```
- `else` block runs if no exception.
- `finally` always runs (cleanup).

---

### 9. Modules & Imports

Organize code into modules (files) and packages (folders with `__init__.py`).

```python
import math
from math import sqrt, pi
import os.path as osp

# Import from your own module
from mymodule import foo
```

---

### 10. Object-Oriented Programming (OOP)

**Classes** encapsulate data and behavior.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"
```
**Magic methods** allow custom behavior for operators/functions:
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```
Now `Vector(1,2) + Vector(3,4)` works, and `print(Vector(1,2))` is nicely formatted.

---

### 11. Closures & Partial Functions

**Closures:** functions generated inside functions, "remember" variables.
```python
def outer(x):
    def inner(y):
        return x + y
    return inner
add5 = outer(5)
add5(10)   # 15
```
**Partial functions:** fix some arguments.
```python
from functools import partial
pow2 = partial(pow, 2)  # pow2(y) = pow(2, y)
```

---

### 12. Decorators

Functions that wrap other functions to add behavior.
```python
from functools import wraps

def timer(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        import time
        start = time.time()
        result = fn(*a, **k)
        print("Elapsed:", time.time() - start)
        return result
    return wrapper
```
Decorators are heavily used in frameworks (Flask, FastAPI, Django) for routing, logging, etc.

---

### 13. Context Managers

Control setup/teardown for resources.
```python
from contextlib import contextmanager

@contextmanager
def my_cm():
    print("enter")
    yield
    print("exit")

with my_cm():
    print("inside")
```
Use for files, locks, DB connections, etc.

---

### 14. itertools & Useful Built-ins

`itertools` provides advanced iteration functions.
```python
from itertools import groupby, chain, combinations, permutations, islice

list(chain([1,2],[3,4]))              # [1,2,3,4]
list(combinations([1,2,3], 2))        # [(1,2),(1,3),(2,3)]
list(permutations("abc", 2))          # [('a','b'),('a','c'),('b','a'),...]
list(islice(range(100), 10, 20))      # [10,11,...,19]
```
**Common built-ins:**
- `all()`, `any()`, `sum()`, `sorted()`, `reversed()`, `enumerate()`, `zip()`, `map()`, `filter()`

---

### 15. Type Hints & Annotations

Type hints help with large codebases, readability, and catching bugs early.
```python
from typing import List, Dict, Optional, Callable, Any, Tuple, Union

def f(a: int, b: str, lst: List[int]) -> Optional[str]:
    ...
def g(cb: Callable[[int], str]) -> None:
    ...
```
Use tools like `mypy` or Pyright for static type checking!

---

### 16. Concurrency

#### Threading (I/O-bound concurrency)
```python
import threading

def worker():
    print("Working")
t = threading.Thread(target=worker)
t.start()
t.join()
```
#### AsyncIO (async/await, scalable I/O)
```python
import asyncio

async def main():
    await asyncio.sleep(1)

asyncio.run(main())
```
Use threading for blocking I/O, asyncio for high-scale concurrent I/O (web servers, async DB).

---

### 17. Standard Library Modules (for Backend)

- `os`, `sys`, `pathlib` — file and OS operations
- `subprocess` — run shell commands
- `logging` — robust logging (always prefer over `print`)
- `json`, `csv`, `pickle` — serialization
- `datetime`, `time` — date/time utilities
- `re` — regular expressions
- `uuid` — unique IDs
- `secrets` — secure random numbers
- `functools` — lru_cache, partial, reduce, etc.
- `heapq`, `bisect`, `array` — advanced data structures
- `typing` — type hints

---

### 18. Best Practices (Backend Focus)

- Use virtual environments (`venv`, `virtualenv`) for dependency isolation.
- Prefer logging to print statements for production.
- Always use context managers (`with`) for file/network/database/resource access.
- Avoid mutable default arguments in function signatures.
- Write docstrings (`"""..."""`) for all public modules/classes/functions.
- Use type hints.
- Use exceptions for error handling, not return codes.
- Profile and benchmark with `cProfile` and `timeit`.
- Unit test your code (`unittest`, `pytest`).
- Write modular, reusable, and readable code.

---

