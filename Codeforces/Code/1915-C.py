for _ in range(int(input())):
    for _ in range(3):
        s = input()
        if s.count('?'):
            if s.count('C') == 0: print('C')
            if s.count('B') == 0: print('B')
            if s.count('A') == 0: print('A')
