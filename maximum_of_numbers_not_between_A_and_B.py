n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
m=0
for j in a:
    if j not in range(x,y):
        if j>m:
            m=j
if m==0:
    print('-1')
else:
    print(m)