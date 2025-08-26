D = int(input())
N = int(input())

c = [0] * (D+2)

for _ in range(N):
    L, R = map(int, input().split())
    c[L] += 1
    c[R+1] -= 1

for i in range(1, D+1):
    c[i] += c[i-1]

print('\n'.join(map(str, c[1:D+1])))
