n = int(input())
l = list(map(int, input().split()))
l2 = []

for i in range(n):
    for j in range(i, n):
        l2.append(sum(l[i:j+1]))

print(max(l2))
