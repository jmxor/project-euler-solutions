import math


def triangle_number_generator():
    """Returns a generator object that yields consecutive triangle numbers"""
    i = 1
    num = 0
    while True:
        num += i
        i += 1
        yield num


def num_divisors(n):
    """Returns the number of divisors of n"""
    sqrt = math.floor(math.sqrt(n))
    count = 0
    for i in range(1, sqrt+1):
        if n % i == 0:
            count += 2
    return count


if __name__ == '__main__':
    for n in triangle_number_generator():
        if num_divisors(n) > 500:
            print(n)
            break
