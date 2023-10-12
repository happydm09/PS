for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    num = 0
    
    for _ in range(10):
        if b in a: print(num); break
        
        num += 1
        a += a
    else: print(-1)
