for _ in range(int(input())):
    a, b = map(int, input().split())
    print('Alice' if (a + b) % 2 else 'Bob')
