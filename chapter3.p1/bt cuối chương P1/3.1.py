a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
import math
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))
x=math.sqrt(S)
if (a+b)>c:
    print("Dien tich=", round(x,3), sep="")
elif (a+c)>b:
    print("Dien tich=", round(x,3), sep="")
elif (b+c)>a:
    print("Dien tich=", round(x,3), sep="")
else:
    print("Khong hop le").