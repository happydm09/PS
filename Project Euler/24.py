from itertools import *

l = list(permutations([str(i) for i in range(10)], 10))
print(''.join(l[1000000 - 1]))

# Answer: 2783915460
# Place: 119506th
