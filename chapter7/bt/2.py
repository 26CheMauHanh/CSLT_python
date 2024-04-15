#Viết chương trình:
#Cho phép nhập vào một chuỗi ký tự bất kỳ;
#Cho phép nhập vào một chuỗi ký tự bất kỳ;
#+Không bắt đầu và kết thúc bằng các ký tự trắng;
#+Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng
#+Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
#+Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;
#In nội dung chuỗi sau khi xử lý lên màn hình.
#INPUT:Xin Chào , tôi là    sInh viêN
#OUTPUT:Xin chào, tôi là sinh viên
def LamSachChuoi(st):
    a=st
    a1=a.strip()
    a2=a1.capitalize()
    a3=" ".join(a2.split())
    a4=a3.replace(" , ",", ")
    return a1,a2,a3,a4

st=input()
a1,a2,a3,a4=LamSachChuoi(st)

print(a4)