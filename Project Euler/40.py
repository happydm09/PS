n = '0'
i = 1

while len(n) < 1000001:
    n += str(i)
    i += 1

print(int(n[1]) * int(n[10]) * int(n[100]) * int(n[1000]) * int(n[10000]) * int(n[100000]) * int(n[1000000]))

# Answer: 210
# Place: 83719th
