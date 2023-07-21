for _ in range(int(input())):
    a, b, c = map(int, input().split())

    for i in [a + b, a + c, b + c]:
        if i >= 10: print('YES'); break
    else: print('NO')
