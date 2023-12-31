for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    b = 1
    for i in a: b *= i
    
    o = 2023 // b
    if o * b == 2023: 
        l = [o]
        for i in range(k - 1): l.append(1)
        print('YES')
        print(' '.join(list(map(str, l))))
    else: print('NO')
