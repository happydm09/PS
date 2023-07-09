s = []
n = []

for _ in range(int(input())):
    name = input()
    if name in n:
        s[n.index(name)] += 1
    else:
        s.append(1)
        n.append(name)

print(n[s.index(max(s))])
