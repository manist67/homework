loop_n = 0

cache = [None] * 40
cache_count = [0] * 40


def fib(n):
    for i in range(2, n):
        cache_count[i] += 2**(i-2)

    if cache[n-1] is not None:
        return cache[n-1]

    if n == 1 or n == 2:
        return 1
    else:
        cache[n-1] = fib(n-1) + fib(n-2)
        return cache[n-1]


def fibonacci(n):
    global loop_n
    f = [1, 1]
    i = 2
    while i < n:
        loop_n += 1
        f.append(f[i-1] + f[i-2])
        i += 1

    return f[n-1]


n = int(input())
fib(n), fibonacci(n)
recursive_n = 0
for i in cache_count:
    recursive_n += i

print("{} {}".format(recursive_n, loop_n))

