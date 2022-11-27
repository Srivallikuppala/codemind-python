a=input()
b=list(a)
c=0
for i in b:
    if i.isdigit():
        c+=int(i)
print(c)