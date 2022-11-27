n=input()
x=list(n)
s=0
for i in x:
    if i.isdigit():
        s+=int(i)
print(s)