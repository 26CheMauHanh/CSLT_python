def Nhap():
    print("Nhap hai canh ke cua tam giac vuong:")
    a=int(input())
    b=int(input())
    return a,b

def Tinh(a,b):
    import math
    n=a**2+b**2
    x=math.sqrt(n)
    return x

def InKQ(a,b,x):
    print("Canh ke thu nhat la:",str(a)+",", "canh ke thu hai:",str(b)+",", "co canh huyen =",round(x,2))

a,b=Nhap()
x=Tinh(a,b)
InKQ(a,b,x)