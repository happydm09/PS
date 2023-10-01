def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
        if len(box) == 10001: return box[-1]
    return box
    
print(SOE(10000000))

# Answer: 104743
# Place: 430701st
