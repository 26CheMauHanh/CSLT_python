import math
def LaSoNguyenTo(x):
    if x<2:
       return False       
    for i in range(2,int(math.sqrt(x)+1)):
       if x%i==0:
           return False
    return True
def SoHopLe(x):
    if x<=1:
        return True
    return False
def NhapVaDem():
    kq=0
    x=int(input())
    while SoHopLe(x)==False and LaSoNguyenTo(x)==True:
        kq=kq+1
        SoHopLe(x)
        LaSoNguyenTo(x)
        NhapVaDem() 
    return x
def InKQ(kq): 
    print("Co",kq,"so nguyen to")

print("Nhap day so:")
kq=NhapVaDem()
InKQ(kq)