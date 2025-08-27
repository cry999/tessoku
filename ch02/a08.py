H, W = map(int, input().split())

X = [
    list(map(int, input().split())) for _ in range(H)
]

cum = [[0] * (W+1) for _ in range(H+1)]

for i in range(H):
    for j in range(0, W):
        cum[i+1][j+1] = cum[i+1][j] + X[i][j]

# print(cum)

for j in range(W+1):
    for i in range(H):
        cum[i+1][j] += cum[i][j]

# print(cum)

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(cum[C][D] - cum[C][B-1] - cum[A-1][D] + cum[A-1][B-1])
