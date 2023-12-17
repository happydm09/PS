from collections import *

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

box = SOE(1000000)
n = 0

for i in box:
    l = deque(list(str(i)))

    for _ in range(len(l)):
        l.rotate()
        a = int(''.join(l))
        if BS(a, box) == 0: break
    else: n += 1

print(n)

# Answer: 55
# Place: 88992nd
