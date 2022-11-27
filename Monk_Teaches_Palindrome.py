for i in range(int(input())):
    a=input()
    a=list(a)
    r=a[::-1]
    if a==r and len(a)%2==0:
        print('YES EVEN')
    elif a==r and len(a)%2!=0:
        print('YES ODD')
    else:
        print('NO')