n=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
for i in range(n-1):
    if i%2==0:
        temp=b[i+1]
        b[i+1]=b[i]
        b[i]=temp
print(*b)
