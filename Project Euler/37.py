n = 0
a = 10

def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

def BS(target, data):
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return 1
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return 0

b = SOE(2000000)

for i in b:
    s = str(i)
    f = 1

    for j in range(len(s)-1):
        new = int(s[j+1:])
        if BS(new, b) == 0: break
    else: f = 0

    if f: continue


    for j in range(len(s)-1):
        new = int(s[:j+1])
        if BS(new, b) == 0: break
    else: n += i

print(n - 17)

# Answer: 748317
# Place: 77422nd
