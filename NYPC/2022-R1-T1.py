N, M = map(int, input().split())
ci = 0

for _ in range(M):
    t, i, s = map(int, input().split())
    if t < 60:
        print('NO')
        break
    if i == ci:
        print('NO')
        break
    ci = i
else:
    print('YES')
