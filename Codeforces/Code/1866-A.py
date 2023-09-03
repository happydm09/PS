input(); a = list(map(int, input().split()))
print(abs(sorted(a, key=abs)[0]))
