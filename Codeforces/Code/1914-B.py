from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    log = [1]

    l = deque([i+1 for i in range(n)])
    a = n-k+1

    if k == 0: print(*list(l)[::-1]); continue

    l.popleft()

    while a != n+1:
        l.pop()
        log.append(a)
        a += 1
    for i in range(len(l)): log.append(l.pop())

    print(' '.join(list(map(str, log))))
