#Viết chương trình:
#-Nhập vào một chuỗi ký tự chứa họ tên và email;
#-Chương trình thực hiện tách email từ chuỗi trên và in kết quả lên màn hình;
#-Biết rằng dữ liệu nhập vào có email hoặc không có email.
#Vídụ:
#Ho ten: Nguyen Van An, Email: vanan@gmail.com
#Ho ten: Le Ngoc Binh, Email:
#Ho ten: Pham Anh Ngoc, Email: anhngoc@gmail.com
#TEST1:
#Input:Ho ten: Nguyen Van An, Email: vanan@gmail.com
#Output:vanan@gmail.com
#TEST2:
#Input:Ho ten: Le Ngoc Binh, Email:
#Output:
str=input()
x=str.split("Email: ")
if len(x)==1:
    print()
else:
    print(x[1])