for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    l = sorted([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], key=lambda x: (x[0], x[1]))

    a = l[1][1] - l[0][1]
    print(a ** 2)
