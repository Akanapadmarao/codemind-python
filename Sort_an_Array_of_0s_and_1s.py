n=int(input())
m=list(map(int,input().split()))
l=[]
zero=m.count(0)
ones=m.count(1)
for i in range(zero):
    l.append(0)
for i in range(ones):
    l.append(1)
print(*l)