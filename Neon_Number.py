n=int(input())
s=n**2
a=0
while s!=0:
    d=s%10
    a+=d
    s=s//10
if a==n:
    print("Neon Number")
else:
    print("Not Neon Number")