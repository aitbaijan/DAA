# Recursive Binary Search

## 1. Description
Recursive Binary Search uses the divide-and-conquer strategy by making recursive function calls to evaluate left or right search halves.

## 2. Approach & Call Tracing Example

Array: `arr = [1, 3, 5, 7, 9, 11, 13, 15]`

### Search Target = 13
1. **Call 1:** `binary_search_recursive(arr, 13, low=0, high=7)`
   - `mid = 3`, `arr[3] = 7`.
   - $7 < 13 \rightarrow$ Calls `binary_search_recursive(arr, 13, low=4, high=7)`.
2. **Call 2:** `binary_search_recursive(arr, 13, low=4, high=7)`
   - `mid = 5`, `arr[5] = 11`.
   - $11 < 13 \rightarrow$ Calls `binary_search_recursive(arr, 13, low=6, high=7)`.
3. **Call 3:** `binary_search_recursive(arr, 13, low=6, high=7)`
   - `mid = 6`, `arr[6] = 13`.
   - $13 == 13 \rightarrow$ Target found, returns index `6`.

## 3. Complexity Analysis
- **Time Complexity:** $O(\log N)$ — The array search space halves at every call.
- **Space Complexity:** $O(\log N)$ — Stack space consumed by recursive function call frames.
