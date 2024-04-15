#Viếtchương trình có sử dụng hàm thực hiện các yêu cầu sau:
#-Hàm Input(): nhập một số nguyên n(n>0)và n số nguyên lưu vào List L,và mộtsố nguyên x;
#-Hàm FirstAndLast(L) trả về và in lên màn hình List mới chỉ gồm phần tử đầu tiên và cuối cùng của L
#-Hàm Search(L,x): xác định xcó nằm trong Lhay không. Trả về Truenếu tìm thấy, còn lại trả về False.
#TEST:
#n=4
#3
#5
#3
#7
#x=5
#[3, 7]
#True
def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        b=int(input())
        L=L+[b]
    x=int(input("x="))
    return L,x

def FirstAndLast(L):
    global A,B,C
    B=L[0]
    C=L[-1]
    A=[B]+[C]
    print(A)
    return A
    
def Search(L,x):
    if x in L:
        print("True")
    else:
        print("False")

L,x=Input()
F=FirstAndLast(L)
Search(L,x)