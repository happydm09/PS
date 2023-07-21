for _ in range(int(input())):
    s = ''
    for i in [input() for _ in range(8)]:
        for c in i:
            if c != '.': s += c
    print(s)
