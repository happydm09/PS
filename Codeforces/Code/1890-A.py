for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 'NO'

    if len(set(a)) == 2:
        l = list(set(a))
        x, y = a.count(l[0]), a.count(l[1])

        if n % 2 == 0:
            if x == y: ans = 'YES'
        else:
            if abs(x - y) == 1: ans = 'YES'

    if len(set(a)) == 1: ans = 'YES'

    print(ans)
