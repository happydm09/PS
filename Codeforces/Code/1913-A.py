for _ in range(int(input())):
    s = input()
    a, b, f = "", "", 0

    for i in s:
        if f: b += i
        else:
            if a != "" and i != '0':
                f = 1
                b += i
            else: a += i
    try:
        if int(a) < int(b): print(a, b)
        else: print(-1)
    except: print(-1)
