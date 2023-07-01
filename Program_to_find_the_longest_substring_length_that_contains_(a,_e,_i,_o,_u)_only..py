s=input()
l=[]
c=0
a="aeiouAEIOU"
for i in s:
    if i in a:
        c+=1
    else:
        c=0
    l.append(c)
print(max(l))
    
