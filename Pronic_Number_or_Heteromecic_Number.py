n=int(input())
r=1
c=0
for i in range(1,n):
    r=i*(i+1)
    if n==r:
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")