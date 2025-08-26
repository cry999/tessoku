N = int(input())
A = list(map(int, input().split()))
B = [0] * (N+1)  # B[i] は i 回目までにあたりを引いた回数
for i in range(N):
    B[i+1] = B[i] + A[i]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    wins = B[R] - B[L-1]
    times = R - (L - 1)
    lose = times - wins

    if wins > lose:
        print('win')
    elif wins < lose:
        print('lose')
    else:
        print('draw')
