def f(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    return fa
n=int(input())
m=n
s=0
while n!=0:
    d=n%10
    s+=f(d)
    n=n//10
if m==s:
    print("The number",m,"is a strong number")
else:
    print("The number",m,"is not a strong number")