#In ra tất cả số trong mảng A cùng với số lần xuất hiện của chúng
def Input():
    n=int(input())
    A=[]
    for i in range(1,n+1):
        x=int(input())
        A=A+[x]
    return A,n

def