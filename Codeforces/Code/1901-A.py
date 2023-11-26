for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    q = a[0]

    for i in range(n - 1):
        c = a[i + 1] - a[i]
        if c > q: q = c

    print(max(q, (x - a[-1]) * 2))
