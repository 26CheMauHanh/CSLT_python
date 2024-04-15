import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))
x=math.sqrt(s)
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Dien tich=",round(x,3),sep="")
else:
    print("Khong hop le")