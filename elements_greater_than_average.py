n=int(input())
a=list(map(int,input().split()))
m=0
avg=sum(a)//n
for j in a:
    if avg<=j:
        m+=1
    
print(m)