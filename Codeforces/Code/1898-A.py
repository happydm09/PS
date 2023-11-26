for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    
    b = s.count('B')
    if b == k: print(0)
    elif b < k:
        print(1)
        for i in range(n):
            s[i] = 'B'
            b = s.count('B')
            if b == k:
                print(i+1, 'B')
                break
    else:
        print(1)
        
        for i in range(n):
            s[i] = 'A'
            b = s.count('B')
            if b == k:
                print(i+1, 'A')
                break
            
