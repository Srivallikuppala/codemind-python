def pr(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n1=int(input())

for i in range(n1):
    n=int(input())
    np=n
    pp=0
    for j in range(n,1,-1):
        if pr(j):
            pp=j
            break
    while pr(np)==False:
        np+=1
    if np-n>=n-pp:
        print(pp)
    else:
        print(np)