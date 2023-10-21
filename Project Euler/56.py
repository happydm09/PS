ans = 0

for a in range(1, 100):
    for b in range(1, 100):
        n = a ** b
        num = 0
        
        for i in str(n): num += int(i)
        if num > ans: ans = num
        
print(ans)

# Answer: 972
# Place: 60947th
