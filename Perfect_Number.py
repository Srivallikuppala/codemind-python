def div(x):
    s=0
    for i in range (1,x):
        if(x%i==0):
            s=s+i
    return s

x=int(input())
d=div(x)
if x==d:
    print("True")
else:
    print("False")