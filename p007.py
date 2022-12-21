"""Problem 007 - 10001st prime"""

from math import log


def erato_sieve(n: int) -> list[int | None]:
    """"""
    numbers = list(range(0, n))
    i = 2
    for i in range(2, int(n**0.5) + 1):
        if not numbers[i]:
            continue
        for j in range(i**2, n, i):
            numbers[j] = None
    return list(filter(lambda x: bool(x), numbers))


if __name__ == '__main__':
    n = 10_001
    limit = int(n * log(n) + n * log(log(n)))
    primes = erato_sieve(limit)
    print(primes[10001])

