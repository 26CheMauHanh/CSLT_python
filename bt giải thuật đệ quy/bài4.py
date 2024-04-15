class SinhVien:
    def _init_(self, MaSV, hoten, diem1,diem2):
        self.MaSV=MaSV #thuộc tính đối tượng
        self.Hoten=hoten
        self.Diem1=diem1
        self.Diem2=diem2
        self.DiemTB=(diem1 + diem2)/2
    def InSV(self):
        print(self.MaSv)
        print(self.Hoten)
        print(self.Diem1)
        print(self.Diem2)
        print(self.DiemTB)
        