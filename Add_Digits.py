
def gS(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return str(sum)
n=input()
while len(n)!=1:
    n=gS(n)
    
print(n)

