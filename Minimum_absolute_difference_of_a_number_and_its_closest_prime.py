def pr(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
np=n
pp=0
for i in range(n,1,-1):
    if pr(i):
        pp=i
        break
while pr(np)==False:
    np+=1
if np-n<n-pp:
    print(np-n)
else:
    print(n-pp)