n=int(input())
rev=0
t=n
if n<0:
    n=n*(-1)
while n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
    
if(t<0):
    print(-rev)
else:
    print(rev)