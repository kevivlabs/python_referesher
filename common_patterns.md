# Python Built-in Data Structures and Methods for LeetCode Problem Patterns

This guide maps common LeetCode problem types to Python’s built-in data structures and their methods, along with typical patterns and example methods you’ll use. Use this as a quick reference to choose the right tool for the job!

---

## 1. **Arrays/Lists (`list`)**

**When to use:**  
- Sequential data, random access, stack/queue emulation, sliding window, two pointers, sorting, prefix/suffix operations.

**Key Methods/Patterns:**  
- `append()`, `pop()`, `extend()`, `insert()`, `remove()`, `index()`, `sort()`, `reverse()`, slicing (`arr[:]`)
- Two pointers: `left`, `right` indices
- Sliding window: move `left` and `right` over array
- Reversing: `arr[::-1]`, `arr.reverse()`
- Sorting: `arr.sort()`, `sorted(arr, key=...)`
- Stack: `append()`, `pop()`
- Queue: `collections.deque`

**LeetCode Patterns:**  
- Two Sum, 3Sum, Max Subarray, Sliding Window Maximum, Move Zeroes, Container With Most Water

---

## 2. **Hash Map (`dict`)**

**When to use:**  
- Fast lookup, counting, mapping, frequency tables, caching, grouping

**Key Methods/Patterns:**  
- `get(key, default)`, `setdefault(key, default)`, `.items()`, `.keys()`, `.values()`
- Counting/frequency:  
  `d = {}`  
  `for x in arr: d[x] = d.get(x, 0) + 1`
- Grouping: Group anagrams, categorize items by some attribute

**LeetCode Patterns:**  
- Two Sum, Group Anagrams, Longest Substring Without Repeating Characters, Top K Frequent Elements, Valid Anagram

---

## 3. **Hash Set (`set`)**

**When to use:**  
- Fast membership test, removing duplicates, intersections, unions, unique elements

**Key Methods/Patterns:**  
- `add()`, `remove()`, `discard()`, `in`, `|` (union), `&` (intersection), `-` (difference)
- Used for:  
  - Detecting duplicates
  - Finding intersection/union of arrays
  - Unique substrings/subarrays

**LeetCode Patterns:**  
- Contains Duplicate, Happy Number, Intersection of Two Arrays, Longest Consecutive Sequence, Unique Email Addresses

---

## 4. **Stack (via `list` or `collections.deque`)**

**When to use:**  
- LIFO problems, parsing, backtracking, DFS, balanced parentheses, evaluate expressions, undo/redo

**Key Methods/Patterns:**  
- `append()`, `pop()`
- Used for:  
  - Parentheses matching
  - Monotonic stack (for next greater/smaller element)
  - DFS traversal (iterative)
  
**LeetCode Patterns:**  
- Valid Parentheses, Daily Temperatures, Min Stack, Evaluate Reverse Polish Notation, Largest Rectangle in Histogram

---

## 5. **Queue (via `collections.deque`)**

**When to use:**  
- FIFO problems, BFS, level order traversal of trees/graphs, sliding window

**Key Methods/Patterns:**  
- `append()`, `popleft()`, `appendleft()`, `pop()`
- Used for:  
  - BFS
  - Level order traversal
  - Sliding window maximum

**LeetCode Patterns:**  
- Binary Tree Level Order Traversal, Rotting Oranges, Course Schedule (BFS), Sliding Window Maximum

---

## 6. **Counter (`collections.Counter`)**

**When to use:**  
- Counting hashable objects, frequency analysis, anagrams

**Key Methods/Patterns:**  
- `Counter(arr)`, `most_common(n)`, arithmetic between counters

**LeetCode Patterns:**  
- Valid Anagram, Top K Frequent Elements, Minimum Window Substring

---

## 7. **Defaultdict (`collections.defaultdict`)**

**When to use:**  
- Grouping, counting, auto-initialized dictionaries

**Key Methods/Patterns:**  
- `defaultdict(list)`, `defaultdict(int)`
- Used for:  
  - Grouping anagrams
  - Building adjacency lists (graphs)
  - Counting without manual key existence check

**LeetCode Patterns:**  
- Group Anagrams, Word Ladder, Course Schedule (Graph Construction)

---

## 8. **Heap (`heapq`)**

**When to use:**  
- Priority queue, top K elements, scheduling, merging sorted lists, min/max tracking

**Key Methods/Patterns:**  
- `heapify()`, `heappush()`, `heappop()`, use `-x` for max-heap

**LeetCode Patterns:**  
- Kth Largest Element in Array, Merge K Sorted Lists, Find Median from Data Stream, Top K Frequent Elements

---

## 9. **Deque (`collections.deque`)**

**When to use:**  
- Double-ended queue, sliding window, both stack and queue operations

**Key Methods/Patterns:**  
- `append()`, `appendleft()`, `pop()`, `popleft()`
- Used for:  
  - Sliding window maximum
  - Monotonic queue

**LeetCode Patterns:**  
- Sliding Window Maximum, Moving Average from Data Stream

---

## 10. **String Methods (`str`)**

**When to use:**  
- Parsing, splitting, joining, reversing, searching, substring problems

**Key Methods/Patterns:**  
- `split()`, `join()`, `replace()`, `find()`, `startswith()`, `endswith()`, `[::-1]` (reverse)

**LeetCode Patterns:**  
- Reverse String, Longest Palindromic Substring, Implement strStr(), Valid Palindrome

---

## 11. **Tuple**

**When to use:**  
- Immutable group of values, keys in dict/set, coordinate pairs

**Key Methods/Patterns:**  
- Used as:  
  - Dict/set keys (for pairs, states in DP)
  - Storing (row, col) for BFS/DFS in grid

**LeetCode Patterns:**  
- Word Search, Shortest Path in Binary Matrix, DP state representation

---

## 12. **Other Useful Built-ins**

- `enumerate()` — for index & value iteration
- `zip()` — parallel iteration of multiple lists
- `sorted()`, `.sort()` — sorting with custom keys
- `map()`, `filter()` — functional programming patterns
- `all()`, `any()` — condition checking

---

## 13. **Patterns Table**

| Problem Type               | Data Structure      | Typical Method(s)          | Example Problem                        |
|----------------------------|--------------------|----------------------------|----------------------------------------|
| Two pointers/sliding window| list, set, dict    | pop, append, in, get       | Longest Substring Without Repeating    |
| Frequency/anagram          | dict, Counter      | get, Counter, most_common  | Group Anagrams, Valid Anagram          |
| BFS/level order traversal  | deque, set         | append, popleft, add       | Rotting Oranges, Course Schedule       |
| Stack/parentheses parsing  | list (as stack)    | append, pop                | Valid Parentheses, Min Stack           |
| Top K / heap               | heapq, Counter     | heappush, heappop, most_common | Top K Frequent Elements, Kth Largest  |
| Backtracking/DFS           | list, set, tuple   | add, pop, in, tuple(state) | Word Search, Permutations              |
| Dynamic Programming (DP)   | dict, set, tuple   | get, tuple as key          | Coin Change, Edit Distance             |
| Graph problems             | defaultdict(list), set, deque | append, add, popleft | Course Schedule, Word Ladder           |

---

## 14. **Key Takeaways**

- **Lists:** Use for sequential, stack, or simple queue operations.
- **Dicts/Sets:** Use for lookups, uniqueness, and fast membership tests.
- **Counter/Defaultdict:** Simplify counting and grouping.
- **Deque/Heapq:** For sliding window, priority queue, and advanced queue/stack needs.
- **String methods:** For parsing, manipulation, and substring problems.
- **Tuples:** For immutable states, especially as keys in dicts/sets.

**Learn to recognize which data structure matches the problem’s needs!**
