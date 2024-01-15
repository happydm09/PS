for _ in range(int(input())):
    n = int(input())
    s, f = input(), input()
    ans = 0

    sc, fc = s.count('1'), f.count('1')

    if sc > fc: ans += sc - fc

    for i in range(n):
        if f[i] == '1' and s[i] == '0': ans += 1

    print(ans)
