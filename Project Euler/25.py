n1, n2 = 1, 2
n = 2

cur = n1 + n2
count = 4

while len(str(cur)) != 1000:
    count += 1
    if cur % 2 == 0: n += cur
    n1 = n2
    n2 = cur
    cur = n1 + n2

print(count)

# Answer: 4782
# Place: 161182nd
