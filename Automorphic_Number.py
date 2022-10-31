n=int(input())
c=0
p=n*n
#print(n)
while n!=0:
   # print(n%10,p%10)
    if(n%10==p%10):
        c=0
        n=n//10
        p=p//10
    else:
        c=1
        break
if c==0:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")