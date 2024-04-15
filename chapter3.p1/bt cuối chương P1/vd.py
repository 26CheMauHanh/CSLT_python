m1=550
m2=750
m3=950
m4=1350
TieuThu=int(input("Tieu thu="))
if TieuThu<=100:
    TienDien=TieuThu*m1
elif TieuThu<=150:
    TienDien=100*m1 + (TieuThu-100)*m2
elif TieuThu<=200:
    TienDien=100*m1 + 50*m2 + (TieuThu-150)*m3
else:
    TienDien=100*m1 + 50*m2 + 50*m3 + (TieuThu-200)*m4
ThanhTien=TienDien*1.1
print("Phai tra=",ThanhTien,sep="")