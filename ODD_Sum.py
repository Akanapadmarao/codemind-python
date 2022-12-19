n=int(input())
s=0
lst=list(map(int,input().split()))
for i in lst:
    if i%2==1:
        s+=i
print(s)