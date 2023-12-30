for _ in range(int(input())):
    a, b, c = map(int, input().split())
    l = [a, b, c]

    for i in set(l):
        if l.count(i) == 1: print(i); break
