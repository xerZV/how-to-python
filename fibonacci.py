def fib(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b += a
        a = tmp_var
    return result


print(fib(10))
