n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=sum(b)-sum(a)
if c>0:
    print(c)
else:
    print(0)