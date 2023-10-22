n = 0


for i in range(1, 1000000):
    if str(i) == str(i)[::-1]:
        b = str(bin(i))[2:]
        if b == b[::-1]: n += i

print(n)

# Answer: 872187
# Place: 92681st
