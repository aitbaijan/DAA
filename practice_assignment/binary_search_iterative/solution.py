def binary_search_iterative(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Search 23: Index = {binary_search_iterative(arr, 23)}")
    print(f"Search 5:  Index = {binary_search_iterative(arr, 5)}")
    print(f"Search 100: Index = {binary_search_iterative(arr, 100)}")
