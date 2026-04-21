def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    for i in range(1, n+1):
        print(fib(i), end=" ")