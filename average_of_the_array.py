n=int(input())
a=list(map(int,input().split()))
x=sum(a)/len(a)
print("{:.2f}".format(x))