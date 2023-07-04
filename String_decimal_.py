t=int(input())
for j in range(t):
    n=input()
    k=0
    for i in n:
        if (ord(i)<48 or ord(i)>57):
            k=1
            break
    if(k!=1):
        print("True")
    else:
        print("False")