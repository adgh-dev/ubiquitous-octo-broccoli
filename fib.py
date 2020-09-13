import time

def find_fib_iter(n):
    rez = [0, 1]
    for i in range(2, n + 1):
        rez.append(rez[i - 1] + rez[i - 2])
    return rez[n]


def find_fib_rec(n):
    if n < 2:
        return n
    else:
        return find_fib_rec(n - 1) + find_fib_rec(n - 2) 


def find_fib_rec_cached(n, cache):
    if n < 2:
        return n
    else:
        if n - 2 not in cache:
            cache[n - 2] = find_fib_rec_cached(n - 2, cache)
        if n - 1 not in cache:
            cache[n - 1] = find_fib_rec_cached(n - 1, cache)
        return cache[n - 1] + cache[n - 2] 


def main():
    x = 35
    start_time = time.perf_counter()
    print(
        find_fib_iter(x)
    )
    mid_time = time.perf_counter()
    print(mid_time - start_time)
    print(
        find_fib_rec(x)
    )
    mid_mid_time = time.perf_counter()
    print(mid_mid_time - start_time)
    print(
        find_fib_rec_cached(x, {})
    )
    end_time = time.perf_counter()
    print(end_time - mid_mid_time)


if __name__ == "__main__":
    main()