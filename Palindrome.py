a=int(input())
n=a
rev=0
while a>0:
    r=a%10
    rev=rev*10+r
    a=a//10
if rev==n:
    print("True")
else:
    print("False")