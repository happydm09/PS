for _ in range(int(input())):
    block = []
    MIN, MAX = 0, 10**9

    for _ in range(int(input())):
        a, x = map(int, input().split())
        if a == 1: MIN = max(MIN, x)
        elif a == 2: MAX = min(MAX, x)
        else: block.append(x)

    m = len(block)
    for i in block:
        if i < MIN: m -= 1
        elif i > MAX: m -= 1

    ans = MAX-MIN+1-m
    print(ans if ans > 0 else 0)
