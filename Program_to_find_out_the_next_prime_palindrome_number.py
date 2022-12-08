def pr(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
            break
    return True
def  pal(n):
    r=0
    re=0
    m=n
    while n!=0:
        r=n%10
        re=(re*10)+r
        n=n//10
    if m==re:
        return True
    else:
        return False
 
n=int(input())
while True:
    n+=1
    if pr(n)==True and pal(n)==True:
        print(n)
        break