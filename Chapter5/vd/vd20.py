#Viết chương trìnhnhập từ bàn phím 10số nguyên, lưu trữ vào 1 List; và nhập một số nguyên x.
# a.Tìm tất cả các phần tử có giá trị bằng 5và thay bằng x. In kết quả lên màn hình;
# b. Xóa tất cả các phần tử có giá trị bằng xxuất hiện trong tập hợp trên.
def Nhap():
    n=int(input("n="))
    L=[]
    print("Moi nhap",n,"so nguyen")
    for i in range(n):
        x=int(input())
        L=L+[x]
        return L

def