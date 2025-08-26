T = int(input())
N = int(input())

c = [0] * T

for _ in range(N):
    L, R = map(int, input().split())
    c[L] += 1
    if R < T:
        c[R] -= 1

for i in range(1, T):
    c[i] += c[i-1]

print('\n'.join(map(str, c)))
