n=int(input())
n1=n
s=[]
while n%10:
    r=n%10
    s.append(r)
    n=n//10
c=0
for i in range(len(s)):
    c=c+s[i]**(len(s)-i)
if c==n1:
    print("True")
else:
    print("False")