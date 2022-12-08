def pr(n):
    if n==1:
        return False
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and pr(i)==False:
        c+=1
print(c)