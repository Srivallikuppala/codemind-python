def ld(n):
    r=n%10
    if r==2 or r==3 or r==9:
        return True
    else:
        return False
        
for i in range(int(input())):
    c=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if ld(j):
            c+=1
    print(c)