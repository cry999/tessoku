board = [
        [0] * 1501 for _ in range(1501)
]
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    board[X][Y] += 1

cum = [
    [0] * 1501
    for _ in range(1501)
]

for i in range(1501):
    cum[i][0] = board[i][0]
    for j in range(1500):
        cum[i][j+1] = cum[i][j] + board[i][j+1]

for j in range(1501):
    for i in range(1500):
        cum[i+1][j] += cum[i][j]

# print([row[:10] for row in cum[:10]])

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(cum[c][d] - cum[c][b-1] - cum[a-1][d] + cum[a-1][b-1])
