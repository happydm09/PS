for _ in range(int(input())):
    n = int(input())
    max_ = [0, 0, 0]

    for i in range(n):
        a, b = map(int, input().split())
        if a < 11 and b > max_[1]:
            max_ = [a, b, i]
    print(max_[2] + 1)
