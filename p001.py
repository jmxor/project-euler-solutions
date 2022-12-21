""" Problem 001 - Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23. What is the
sum of all the multiples of 3 and 5 below 1000?
"""

if __name__ == '__main__':
    # A simple solution to this is the union of the multiples of 3
    # below 1000 and the multiples of 5 below 1000.
    n = 1000
    ans = sum(set(range(0, n, 3)) | set(range(0, n, 5)))
    print(ans)
