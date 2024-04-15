import math 
kq=0
print('Nhap day so:')
while True:   
    def NhapVaDem():
        x=int(input())
        return x
    def SoHopLe(x):
        if x<=1:
            return True
        return False
    def LaSoNguyenTo(x):
        if(x<2):
            return False
        i=2
        for i in range(2,x//2+1):
         if(x%i == 0):
            return False
         i=i+1
        return True
    x=NhapVaDem()
    SoHopLe(x) 
    if SoHopLe(x) == True:
        break
    if LaSoNguyenTo(x) == True:
        kq=kq+1
    else :
        continue
def InKQ(kq):
    print('Co',kq,'so nguyen to')
InKQ(kq)