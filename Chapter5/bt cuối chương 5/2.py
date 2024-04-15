#Viết chương trình có sử dụng hàm thực hiện các yêu cầu sau:
#-Hàm Input():nhập một số nguyên  n(n>0) và n số nguyên lưu trữ vào một List L;
#-Hàm Search(L): Tìm và trả về số nhỏ nhất và lớn nhất trongList L;
#-Hàm Output(max, min): In lên màn hình số lớn nhất max và bé nhất min;
#Lưu ý:không được sử dụng hàmchuẩnmax()và min()trong Python.
#TEST:
#n=5
#10
#15
#3
#2
#7
#15  2
def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        x=int(input())
        L=L+[x]
    return L,n

def Search(L):
    max=L[0]
    min=L[0]
    for i in range(len(L)):
        if L[i]>max:
            max=L[i]
        elif L[i]<min:
            min=L[i]
    return(max,min)

def Output(max,min):
    print(max,min)

L,n=Input()
max,min=Search(L)
Output(max,min)