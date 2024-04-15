import math
def Nhap():
    n=int(input("n="))
    return n

def LaSNT(n):
    if n<2:
        return False
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if(n%i) == 0:
            return False
    return True

print("Cac so nguyen to:")
if n>=2:
    print(2)
    for i in range(3,n+1):
        if LaSNT(i):
            print(i)
        i=i+2
    
def InKQ()