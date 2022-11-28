def n_p(n):
    c=0
    for i  in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            c=1
            break
    if c==1:
        return True
    else:
        return False
n=int(input())
m=int(input())
r=n+m+1
#print(r)
while n_p(r)==True:
    r=r+1
    #print(r)
if n_p(r)==False:
    print(r-m-n)
    