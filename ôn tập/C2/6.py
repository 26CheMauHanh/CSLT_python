ten=input("Ho ten: ")
nc=int(input("So ngay cong: "))
dg=int(input("Don gia ngay cong: "))
hs=float(input("He so phu cap: "))
tu=int(input("Tam ung: "))
L=dg*nc*hs
TL=L-tu
print("Nhan vien ",ten,", ","Co tien luong=",round(L,1)," va Thuc linh=",round(TL,1),sep="")