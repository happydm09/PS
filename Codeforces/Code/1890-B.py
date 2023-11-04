def goodStr(s):
    pre = ''

    for i in range(len(s)):
        if s[i] == pre: return i
        pre = s[i]

    return '1'

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    t = input()
    ans = 'NO'

    if goodStr(s) == '1': ans = "YES"
    elif goodStr(t) == '1':
        i = goodStr(s)
        if i == '1': ans = "YES"
        for j in range(n):
            s = s[:i] + t + s[i:]
            re = goodStr(s)
            if re == '1': ans = "YES"; break
            i = re

    if n == 1: ans = "YES"

    print(ans)
