class SinhVien:
  def __init__(self, MaSV, name, d1, d2):
    self.MaSV = MaSV
    self.HoTen = name
    self.Diem1= d1
    self.Diem2= d2
    self.DiemTB = None
    self.next = None
class ManageSinhVien:
  listSinhVien=[]
#nhập danh sách gồm n SV
  def nhapSinhVien(self):
    MaSV= input("nhap ma sinh vien: ")
    name=input("nhạp ten sinh vien: ")
    d1=float("nhap diem1: ")
    d2=float("nhap diem2: ")
    sv=SinhVien(MaSV, name,d1,d2)

  def InSinhVien(self):
    print('Hello', self.MaSV,self.HoTen,  self.Diem1,self.Diem2, self.DiemTB)

  def TinhDiemTB(self):
    if (self.Diem1 is not None) and (self.Diem2 is not None):
      self.DiemTB= (self.Diem1+ self.Diem2)/2
    else:
        print('Chua co diem, nen chua tinh duoc trung binh')
       
  def CapNhatSV(self, hoten =None, d1=None, d2=None):
    if hoten is not None:
      self.HoTen = hoten
    if d1 is not None:
      self.Diem1= d1
    if d2 is not None: 
      self.Diem2= d2
#---------------------------------------------------------------------------
class DSSinhVien:
   def __init__(self):
      self.head = None
      self.last = None
   
   def InDSSinhVien(self):
     sv=self.head
     while sv is not None:
         sv.InSinhVien()
         sv=sv.next
   def  NhapDSSinhVien(self):  
      print('số SV cần nhập')
      n= int(input())
      for i in range(n):
        print('Vui long nhap thoong tin SV thu', i)
        print('Mã SV')
        maSV=input()
        print('Ho ten')
        name=input()
        print('Diem 1')
        d1=float(input())
        print('Diem 2')
        d2=float(input())
        newSV= SinhVien(maSV,name,d1,d2)
        newSV.InSinhVien()
        if self.head is None:
           self.head=newSV
        else:
            newSV.next=self.head
            self.head=newSV
#Tính cột điểm TB cho SV đó
   def TinhDiemTBSinhVien (self):
      sv=self.head
      while sv is not None:
         sv.TinhDiemTB()
         sv=sv.next
         sv.DiemTB= (sv.Diem1+ sv.Diem2)/2
#In ra DS SV
   def showSinhVien(self,listSinhVien):
      if (listSinhVien._len_()>0):
        for sv in listSinhVien:
          print("MaSV, name, d1,d2")
#xóa SV tên bất kỳ
   def deleteByname(self,name):
      isDeleted=False
      sv=self.findByname(name)
      if (sv!=None):
        self.listSinhVien.remove(sv)
        isDeleted=True
      return isDeleted
#tính điểm TB của Diem1, Diem2
   def tinhDTB(self, Diem1, Diem2):
      diemTB=(Diem1+Diem2)/2

#Xóa toàn bộ DS    
   def deleteListSinhVien(self,listSinhVien):
      sv=self.findListSinhVien(listSinhVien)
      if sv==None:
        print("Khong tim thay sinh vien.")
      else:
        self.listStudent.remove(sv)
        print("Da xoa toan bo danh sach.")



l=DSSinhVien()
l.NhapDSSinhVien()
l.InDSSinhVien()
