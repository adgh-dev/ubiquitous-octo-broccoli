import time

def find_factorial_iter(n):
    rez = 1
    for i in range(1, n + 1):
        rez = rez * i
    return rez


def find_factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_rec(n - 1)

def find_factorial_rec_cached(n, cache):
    if n == 1:
        return 1
    else:
        if n not in cache:
            cache[n] = n * find_factorial_rec_cached(n - 1, cache)
        return cache[n]



def main():
    x = 100
    start_time = time.perf_counter()
    print(
        find_factorial_iter(x)
    )
    mid_time = time.perf_counter()
    print(mid_time - start_time)
    print(
        find_factorial_rec(x)
    )
    mid_mid_time = time.perf_counter()
    print(mid_mid_time - start_time)
    print(
        find_factorial_rec(x)
    )
    end_time = time.perf_counter()
    print(end_time - mid_mid_time)



if __name__ == "__main__":
    main()