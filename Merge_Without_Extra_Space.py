n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    t=p+q
    t.sort()
    print(*t)