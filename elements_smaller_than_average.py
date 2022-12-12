n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
m=0
for i in a:
    if i<=avg:
        m+=1
print(m)