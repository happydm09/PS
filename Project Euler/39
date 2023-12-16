# very slow
d = {}

for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if (p := a + b + c) < 1000:
                l = [a, b, c]
                m = max(l)

                l.remove(m)

                if a ** 2 + b ** 2 == m ** 2:
                    try: d[p] += 1
                    except: d[p] = 1
            else: break

print(sorted(d.items(), key=lambda x: -x[1])[0][0])

# Answer: 840
# Place: 76992nd
