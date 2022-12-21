"""Problem 006 - Sum square difference"""

if __name__ == '__main__':
    n = 100
    print(sum(i for i in range(n + 1))**2 - sum(j**2 for j in range(n + 1)))
