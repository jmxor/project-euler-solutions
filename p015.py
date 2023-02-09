from math import factorial

if __name__ == '__main__':
    distinct_paths = factorial(40) // (factorial(20) ** 2)
    print(distinct_paths)
