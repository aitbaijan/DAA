def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    # Run 3 examples
    print(f"fib(3) = {fibonacci_recursive(3)}")
    print(f"fib(4) = {fibonacci_recursive(4)}")
    print(f"fib(5) = {fibonacci_recursive(5)}")
