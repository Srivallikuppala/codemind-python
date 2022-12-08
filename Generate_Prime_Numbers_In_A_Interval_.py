def pr(n):
    if n==1:
        return False
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
for i in range(n+1,m):
    if pr(i):
        print(i)