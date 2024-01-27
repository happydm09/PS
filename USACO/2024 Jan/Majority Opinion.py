for _ in'0'* int(input()):
 n,h,l=int(input()),list(map(int,input().split())),set()
 for i in range(n):
  b=h[i:i+3]
  for j in b:
   if b.count(j)>1:l.add(j)
 if len(l):print(' '.join(map(str,sorted(l))))
 else:print(-1)
