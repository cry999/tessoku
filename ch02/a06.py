N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N+1)
for i in range(N):
    B[i+1] = B[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(B[R] - B[L-1])
