for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()) )
    
    if a.count(k) != 0: print("YES")
    else: print("NO")
