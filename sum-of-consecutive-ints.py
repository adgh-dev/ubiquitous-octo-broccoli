# f(n) =  - 1 + 2 - 3 + .. + ( - 1) n n

def sum_of_cons(n):
    if n % 2 == 0:
        return (n // 2) * (n + 1)
    else:
        return (n // 2) * (n + 1) + (n // 2 + 1)


def crappy_cum_of_cons(n):
    sum = 0
    for i in range(1, n + 1):
        print(sum, i)
        sum += i
    return sum


def main():
    n = 5
    print(crappy_cum_of_cons(n))
    print(sum_of_cons(n))


if __name__ == "__main__":
    main()