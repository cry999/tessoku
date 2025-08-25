N, K = map(int, input().split())

count = 0
for a in range(1, min(N, K) + 1):
    for b in range(a, min(K - a, N + 1)):
        c = K - a - b
        if c > N:
            continue
        if c < b:
            break
        if a == b == c:
            count += 1
        elif a == b or b == c or a == c:
            count += 3
        else:
            count += 6

print(count)
