n = 0

for i in range(1, 10001):
    s = str(i)
    for _ in range(50):
        s = str(int(s) + int(s[::-1]))
        if s == s[::-1]: break
    else: n += 1

print(n)
# Answer: 249
# Place: 56689th
