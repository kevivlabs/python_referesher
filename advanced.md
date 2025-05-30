# Advanced Python Refresher

---

## 1. Advanced Data Structures

### **Heap (Priority Queue)**
```python
import heapq

# min-heap
h = [3,1,4]
heapq.heapify(h)
heapq.heappush(h, 2)
smallest = heapq.heappop(h)
# max-heap
h = [3,1,4]
h = [-x for x in h]
heapq.heapify(h)
heapq.heappush(h, -2)
max_val = -heapq.heappop(h)
```

### **Stack / Queue**
```python
stack = []
stack.append(1)
stack.pop()

from collections import deque
queue = deque()
queue.append(1)      # enqueue
queue.popleft()      # dequeue
```

### **Linked List (Custom Implementation)**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### **Binary Tree (Custom Implementation)**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### **Trie**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
```

---

## 2. Algorithms & Patterns

### **DFS & BFS (Graph/Tree Traversal)**
```python
# DFS (recursive)
def dfs(node):
    if not node: return
    visit(node)
    for neighbor in node.neighbors:
        dfs(neighbor)

# BFS
from collections import deque
def bfs(start):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

### **Binary Search**
```python
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
```

### **Two Pointers**
```python
left, right = 0, len(arr)-1
while left < right:
    # logic
    left += 1
    right -= 1
```

### **Sliding Window**
```python
l = 0
for r in range(len(arr)):
    # expand window
    while invalid_condition:
        # shrink window
        l += 1
```

---

## 3. Dynamic Programming

### **1D DP**
```python
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = min(dp[i-1]+cost1, dp[i-2]+cost2)
```

### **2D DP (Matrix)**
```python
dp = [[0]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

### **Memoization (Top-Down DP)**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(idx, state):
    # base case
    # recursion
```

---

## 4. Useful Python Idioms

- **Unpacking**: `a, b, *rest = [1,2,3,4]`
- **Enumerate**: `for i, val in enumerate(arr):`
- **Any/All**: `if any(arr): ...`
- **Defaultdict**: 
  ```python
  from collections import defaultdict
  d = defaultdict(list)
  ```
- **Counter**:
  ```python
  from collections import Counter
  Counter(arr)
  ```
- **Sorting by Custom Key**:  
  `arr.sort(key=lambda x: (x[1], -x[0]))`

---

## 5. Sets for Fast Lookup

```python
seen = set()
if x in seen:
    ...
seen.add(x)
```

---

## 6. Generators & Yield

```python
def gen():
    for i in range(5):
        yield i

g = gen()
next(g)
```

---

## 7. Decorators

```python
def decorator(fn):
    def wrapper(*args, **kwargs):
        # pre
        result = fn(*args, **kwargs)
        # post
        return result
    return wrapper
```

---

## 8. Class Advanced

```python
class MyClass:
    __slots__ = ['a', 'b']  # memory optimization
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @classmethod
    def from_list(cls, lst):
        return cls(lst[0], lst[1])
    @staticmethod
    def helper(x):
        return x**2
```

---

## 9. Advanced Built-ins

- `zip_longest` from `itertools`
- `groupby` from `itertools`
- `bisect.bisect_left(arr, x)`
- `map`, `filter`, `reduce`

---

## 10. Tips for Interviews

- Use `heapq` for Kth largest/smallest problems.
- Use `set` and `dict` for O(1) lookup.
- Use `deque` for fast pop from both ends.
- Know recursion base/recursive case.
- Practice common DP patterns (climb stairs, knapsack, edit distance).
- Use custom classes for tree/list nodes.
- Write clean, modular code with docstrings/comments if allowed.

---

## 11. Common LeetCode Patterns

- **Top K Elements**: Use `heapq`
- **Union-Find** (Disjoint Set):
  ```python
  parent = list(range(n))
  def find(x):
      if parent[x] != x:
          parent[x] = find(parent[x])
      return parent[x]
  def union(x, y):
      parent[find(x)] = find(y)
  ```
- **Backtracking**:
  ```python
  def backtrack(path, options):
      if goal:
          res.append(path[:])
          return
      for o in options:
          path.append(o)
          backtrack(path, options)
          path.pop()
  ```

---

