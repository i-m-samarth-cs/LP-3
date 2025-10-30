# Iterative: O(n) time, O(1) space
def fib_iterative_small(n: int) -> int:
    if n <= 1: return 0
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Recursive (with Memoization): O(n) time, O(n) space
def fib_recursive_small(n: int, cache: dict = {1: 0, 2: 1}) -> int:
    if n in cache:
        return cache[n]
    
    # Calculate, cache, and return
    cache[n] = fib_recursive_small(n - 1, cache) + fib_recursive_small(n - 2, cache)
    return cache[n]

# Example Usage:
n = int(input("Enter value of n(nth Fibonacci number): "))
print(f"Fibonacci Number(Iterative): {fib_iterative_small(n)}")
print(f"Fibonacci Number(Recursive): {fib_recursive_small(n)}")