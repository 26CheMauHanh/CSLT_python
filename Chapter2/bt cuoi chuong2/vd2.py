#nhap hai canh ke cua tam giac vuong
import math
print("Nhap hai canh ke cua tam giac vuong:")
x=int(input())
y=int(input())
k=x**2+y**2    
z=math.sqrt(k)  
print("Canh ke thu nhat la:", str(x)+',', "canh ke thu hai:",str(y)+',',"co canh huyen =",round(z,2))