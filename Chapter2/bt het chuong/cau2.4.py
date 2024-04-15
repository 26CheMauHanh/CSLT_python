a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=(a+b+c)/2
import math
dien_tich=s*(s-a)*(s-b)*(s-c)
x=math.sqrt(dien_tich)
print("Dien tich=", x, sep="")