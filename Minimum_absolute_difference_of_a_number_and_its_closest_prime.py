def pal(n):
    d=0
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            d=1
    if d==0:
        return True
    else:
        return False

n=int(input())
#print(n)
np=0
pp=n+1
for i in range(n-1,0,-1):
    if pal(i):
        np=i
        break
while pal(pp)==False:
    pp+=1
#print(np,pp)
if pal(n):
    print('0')
elif n-np>pp-n:
    print(pp-n)
else:
    print(n-np)