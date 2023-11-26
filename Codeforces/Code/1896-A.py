def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) != n or len(a) != n: return "NO"
    if a[0] == 1: return "YES"
    return "NO"

for _ in range(int(input())): print(solve())
