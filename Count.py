n=int(input())
l=list(map(int,input().split()))
a=0
e=0
for i in l:
    if i%2==0:
        a+=1
    else:
        e+=1
print(a,e)