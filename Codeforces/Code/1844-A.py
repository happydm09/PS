for _ in range(int(input())):
    a, b = map(int, input().split())
    i = 0
    while True:
        i += 1
        if not i in [a, b]:
            break
    print(i)
