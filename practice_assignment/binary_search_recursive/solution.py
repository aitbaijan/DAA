def binary_search_recursive(arr: list[int], target: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Search 7: Index = {binary_search_recursive(arr, 7)}")
    print(f"Search 13: Index = {binary_search_recursive(arr, 13)}")
    print(f"Search 10: Index = {binary_search_recursive(arr, 10)}")
