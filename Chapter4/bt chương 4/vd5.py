def LaSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2,x): 
        if x%i==0:
            return False
    return True
   
def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
def NhapVaDem():
    print("Nhap day so:")
    dem=0
    while True:
        x=int(input())
        if SoHopLe(x)==True:
            break
        if LaSoNguyenTo(x)==True:
            dem=dem+1
         
    return dem
def InKQ(kq):
    print("Co",dem,"so nguyen to")

dem=NhapVaDem()
InKQ(dem)