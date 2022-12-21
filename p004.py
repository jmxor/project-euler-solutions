""" Problem 004 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99. Find
the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n: int) -> bool:
    """Return if a number is a palindrome"""
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindrome(prod):
                palindromes.append(prod)
    print(max(palindromes))
