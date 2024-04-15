import math
n=int(input())
if n<2:
    False
x=int(math.sqrt(n))
for i in range(2,x+1):
    if n%i==0:
        False
if n>=2:
    
    