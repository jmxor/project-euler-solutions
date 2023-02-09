collatz_memo = {}
def collatz_sequence_length(n: int) -> int:
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        length += 1
    return length


if __name__ == '__main__':
    max_length = 0
    max_i = 0
    for i in range(1000000):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            max_i = i
    print(max_i)
