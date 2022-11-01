n=int(input())
m=n
p=0
for i in range(1,n):
    if n%i==0:
        p+=i
if p>m:
    print("True")
else:
    print("False")