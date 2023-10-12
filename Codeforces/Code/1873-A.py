def solve():
    s = input()
    a, b, c = s[0], s[1], s[2]
    sort = ''.join(sorted([a, b, c]))
    
    if s == sort: return 'YES'
    if a+c+b == sort or b+a+c == sort or c+b+a == sort: return 'YES'
    
    return 'NO'

for _ in range(int(input())): print( solve())
