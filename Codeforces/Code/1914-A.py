for _ in range(int(input())):
    n = int(input())
    s = input()

    sol = 0

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if s.count(i) >= ord(i) - 64: sol += 1

    print(sol)
