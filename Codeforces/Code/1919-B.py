for _ in range(int(input())):
    n = int(input())
    s = input()

    print(abs(s.count('+') - s.count('-')))
