for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    minus = 0

    for i in a:
        if i < 0: minus += 1
        if i == 0: minus = 1; break

    if minus % 2 == 1: print(0)
    else:
        print(1)
        print(1, 0)
