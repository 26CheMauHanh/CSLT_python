#hãy nhập vào danh sách sv
class SinhVien:
    def _init_(self, MaSV, hoten, diem1,diem2):
        self.MaSV=MaSV #thuộc tính đối tượng
        self.Hoten=hoten
        self.Diem1=diem1
        self.Diem2=diem2
        self.DiemTB=(diem1 + diem2)/2

DSSV=[]
n=100
for i in range(100):
    MaSV=input("Nhap MaSV:")
    Hoten=input("Nhap hoten:")
    Diem1=float(input("Nhap diem mon1:"))
    Diem2=float(input("Nhap diem mon2:"))
    newSV=SinhVien(MaSV,Hoten,Diem1,Diem2)
    DSSV.append(SinhVien)
print(DSSV)
TBM1=0
TBM2=0
for i in range(n):
    TBM1=TBM1+DSSV[i].Diem1
    TBM2=TBM2+DSSV[i].Diem2