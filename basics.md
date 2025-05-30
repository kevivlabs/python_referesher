# Python Interview Syntax & Data Structures Refresher

## 1. Basics

```python
# Variables
x = 10
y = 'hello'

# Functions
def add(a, b):
    return a + b

# Conditionals
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Smaller")

# Loops
for i in range(5):
    print(i)

while x > 0:
    x -= 1

# List Comprehension
squares = [i*i for i in range(5)]
```

---

## 2. Data Structures

### List

```python
arr = [1, 2, 3]
arr.append(4)
arr.pop()            # Removes last
arr.insert(1, 10)
arr.remove(2)        # Removes first 2
arr.sort()
arr.reverse()
arr[0]               # Indexing
arr[:2]              # Slicing
len(arr)
sum(arr)
arr.index(3)
```

### Tuple (Immutable)

```python
t = (1, 2, 3)
t[0]
len(t)
```

### String

```python
s = "hello"
s.upper()
s.lower()
s[::-1]           # Reverse
s.split('e')
''.join(['a','b'])
s.replace('h','y')
s.find('e')
str(123)          # Int to str
int("123")        # Str to int
```

### Set (Unique, Unordered)

```python
st = {1, 2, 3}
st.add(4)
st.remove(3)
st2 = {2, 3, 5}
st | st2          # Union
st & st2          # Intersection
st - st2          # Difference
```

### Dictionary (Key-Value)

```python
d = {'a': 1, 'b': 2}
d['a']
d.get('c', 0)     # Default if not found
d.keys()
d.values()
d.items()
d['c'] = 3
del d['a']
```

---

## 3. Collections

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter
c = Counter([1,1,2,3])
c.most_common(1)

# defaultdict
dd = defaultdict(int)
dd['a'] += 1

# deque
q = deque()
q.append(1)
q.appendleft(2)
q.pop()
q.popleft()

# namedtuple
Node = namedtuple('Node', 'val left right')
n = Node(1, None, None)
```

---

## 4. Common Patterns

- **Iterate with index**:  
  ```python
  for i, val in enumerate(arr):
      print(i, val)
  ```

- **Zip two lists**:  
  ```python
  for a, b in zip(list1, list2):
      print(a, b)
  ```

- **Sorting**:  
  ```python
  arr.sort()                # Ascending
  arr.sort(reverse=True)    # Descending
  arr.sort(key=lambda x: x[1])
  ```

- **Lambda**:  
  ```python
  f = lambda x: x + 1
  ```

---

## 5. Useful Built-ins

- `max(arr)`, `min(arr)`, `sum(arr)`, `abs(x)`, `sorted(arr)`
- `any([True, False])`, `all([True, False])`

---

## 6. Useful Algorithms/Tricks

- **Swapping**:  
  ```python
  a, b = b, a
  ```

- **Reverse list**:  
  ```python
  arr[::-1]
  arr.reverse()
  ```

- **Copying list**:  
  ```python
  arr_copy = arr[:]
  ```

---

## 7. Classes

```python
class MyClass:
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
obj = MyClass(10)
obj.get()
```

---

## 8. Exception Handling

```python
try:
    # risky code
    pass
except ValueError as e:
    print(e)
finally:
    print("Done")
```

---

## 9. Reading Input (for LeetCode)

```python
# Single line
x = input()
# Multiple space-separated
a, b = map(int, input().split())
# List of numbers
arr = list(map(int, input().split()))
```

---

## 10. For LeetCode: Function Signature

```python
def function_name(params):
    # Your code
    return result
```

---

