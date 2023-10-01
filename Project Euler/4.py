def is_pal(s): return s == s[::-1]

n = 0

for i in range(100, 999):
    for j in range(100, 999):
        g = i * j
        if is_pal(str(g)):
            if g > n: n = g
            
print(n)

# Answer: 906609
# Place: 496643rd
