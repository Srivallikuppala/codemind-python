def pr(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
f=0
for i in range(1,n+1):
    if n%i==0:
        if pr(i)==True:
            for j in range(1,n+1):
                if n%j==0 and pr(j)==True and i*j==n and i!=j:
                    f=1
                    print(i,j)
                    break
            if f==1:
                break
if f==0:
    print("-1")