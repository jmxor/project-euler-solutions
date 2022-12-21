""" Problem 003 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
prime factor of 600,851,475,143?"""


def factorise(n: int) -> list[int]:
    """Returns a list of the prime factors of n"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors


if __name__ == '__main__':
    # takes the largest value in the prime factor tree of n
    n = 600_851_475_143
    print(max(factorise(n)))
