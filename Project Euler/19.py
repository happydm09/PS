from datetime import *

n = 0

for i in range(1901, 2001):
    for j in range(1, 13):
        date = datetime(i, j, 1)
        if date.weekday() == 6: n += 1

print(n)

# Answer: 171
# Place: 140045th
