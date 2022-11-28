def is_p(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return False
    else:
        return True
n=int(input())
c1=0
for i in range(1,n+1):
    if n%i==0:
        
        if is_p(i):
            c1+=1
print(c1)