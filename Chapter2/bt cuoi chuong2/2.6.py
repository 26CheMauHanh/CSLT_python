ten=input("Ho ten: ")
ngay=int(input("So ngay cong: "))
gia=int(input("Don gia ngay cong: "))
phu_cap=float(input("He so phu cap: "))
ung=int(input("Tam ung: "))
luong=gia*ngay*phu_cap
thuc_linh=luong-ung
print("Nhan vien ", ten, ", ", "Co tien Luong=",round(luong,1), ", ", "Tam ung=",round(ung,1) , " va ", "Thuc linh=",round(thuc_linh,1), sep="")