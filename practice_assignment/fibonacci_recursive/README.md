# Recursive Fibonacci Algorithm

## 1. Description
The Fibonacci sequence is defined recursively as $F(0) = 0, F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$ for $n > 1$.

## 2. 3 Execution Examples & Call Tree Structure

### Example 1: $n = 3$
* **Result:** `2`
* **Recursive Call Tree:**
```text
fib(3)
├── fib(2)
│   ├── fib(1) -> 1
│   └── fib(0) -> 0
│   └── (1 + 0) -> returns 1
└── fib(1) -> 1
Total: 1 + 1 = 2
```

### Example 2: $n = 4$
* **Result:** `3`
* **Recursive Call Tree:**
```text
fib(4)
├── fib(3)
│   ├── fib(2) -> returns 1
│   └── fib(1) -> returns 1
│   └── (1 + 1) -> returns 2
└── fib(2)
    ├── fib(1) -> returns 1
    └── fib(0) -> returns 0
    └── (1 + 0) -> returns 1
Total: 2 + 1 = 3
```

### Example 3: $n = 5$
* **Result:** `5`
* **Recursive Call Tree:**
```text
fib(5)
├── fib(4) -> evaluates to 3
└── fib(3) -> evaluates to 2
Total: 3 + 2 = 5
```

## 3. Complexity Analysis
- **Time Complexity:** $O(2^n)$ — Exponential growth because function calls branch into two repeated subproblems.
- **Space Complexity:** $O(n)$ — Maximum depth of the recursion call stack is $n$.
