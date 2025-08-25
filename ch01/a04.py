def padding(s: str, n: int, pad: str = '0') -> str:
    return pad * (n - len(s)) + s if len(s) < n else s


def binary(n: int) -> str:
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n >> 1
    return padding(s, 10)


print(binary(int(input())))
