#Thực hiện phép cộng hai phân số.
from fractions import Fraction
a1=int(input("tu1="))
b1=int(input("mau1="))
a2=int(input("tu2="))
b2=int(input("mau2="))
print(Fraction(a1,b1)+ Fraction(a2,b2))