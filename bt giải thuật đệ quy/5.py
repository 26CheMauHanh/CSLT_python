n=int(input())
import math 
def Nt(n):
    t=True
    if n==2:
        print(n)
    else:
        x=int(math.sqrt(n))
        for j in range(2,x+1):
            if n%j==0:
                T=False
            break
        if T==True:
            print(n)
        Nt(n-1)
Nt(n)