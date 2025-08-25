N = input()

ans = 0
for b in N:
    ans = ans << 1
    if b == '1':
        ans += 1

print(ans)
