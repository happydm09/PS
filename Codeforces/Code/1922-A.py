for _ in range(int(input())):
    n = int(input())
    a, b, c = input(), input(), input()

    q = 0

    for i in range(n):
        if c[i] == a[i] or c[i] == b[i]: q += 1

    print("YES" if q != n else 'NO')
