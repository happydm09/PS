def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box
    
print(sum(SOE(2000000)))

# Answer: 142913828922
# Place: 335999th
