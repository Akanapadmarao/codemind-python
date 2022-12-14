n=int(input())#175
temp=n
temp1=n
c=0
su=0
while n>0:
    c=c+1
    n=n//10
i=c
while temp>0 and i>=1:
    re=temp%10
    su=su+pow(re,i)
    i-=1
    temp=temp//10
if temp1==su:
    print("True")
else:
    print("False")