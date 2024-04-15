def Nhap():
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    d=float(input("d="))
    return a,b,c,d

def Tinh(a,b,c,d):
    tong=a+b+c+d
    tb=(a+b+c+d)/4
    return tong,tb

def InKQ(tong,tb):
    print("Tong=",tong,sep="")
    print("Trung binh cong=",tb,sep="")

a,b,c,d=Nhap()
tong,tb=Tinh(a,b,c,d)
InKQ(tong,tb)
