"""Problem 010 - Summation of primes"""


def erato_sieve(n: int) -> list[int | None]:
    """Returns a list of all the primes below n"""
    numbers = list(range(0, n))
    i = 2
    for i in range(2, int(n**0.5) + 1):
        if not numbers[i]:
            continue
        for j in range(i**2, n, i):
            numbers[j] = None
    return list(filter(lambda x: bool(x), numbers))


if __name__ == '__main__':
    n = 2_000_000
    print(sum(erato_sieve(n)))
