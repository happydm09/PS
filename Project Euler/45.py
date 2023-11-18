def T(n): return n * (n + 1) // 2
def P(n): return n * (3 * n - 1) // 2
def H(n): return n * (2 * n - 1)

t, p, h = [], [], []

for i in range(144, 99999):
    t.append(T(i))
    p.append(P(i))
    h.append(H(i))

for i in t:
    if i in p:
        if i in h:
            print(i)
            break

# Answer: 1533776805
# Place: 74320th
