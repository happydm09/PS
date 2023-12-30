import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if math.sqrt(sum(a)).is_integer(): print('YES')
    else: print('NO')
