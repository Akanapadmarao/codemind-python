n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if l.count(i)>1:
        s.append(i)
x=set(s)
print(*x)