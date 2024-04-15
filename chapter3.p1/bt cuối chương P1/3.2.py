m1=int(input("M1="))
m2=int(input("M2="))
m3=int(input("M3="))
tieu_thu=int(input("S="))
if tieu_thu<=100:
    tien_dien=tieu_thu*m1
elif tieu_thu<=150:
    tien_dien=100*m1 + (tieu_thu-100)*m2
else:
    tien_dien=100*m1 + 50*m2 + (tieu_thu-150)*m3
print("Phai tra=", tien_dien, sep="")