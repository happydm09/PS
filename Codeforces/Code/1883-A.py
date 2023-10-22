for _ in range(int(input())):
    num = 0
    cur = 1

    for i in input():
        i = int(i)
        if i == 0: i = 10
        num += abs(i - cur) + 1

        cur = i

    print(num)
