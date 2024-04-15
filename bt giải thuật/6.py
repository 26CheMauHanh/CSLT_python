#Tìm phần tử lớn nhất của một dãy gồm n số nguyên
def Input():
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        x=int(input())
        L=L+[x]
    return L,n

def Search(L):
    max=L[0]
    for i in range(len(L)):
        if L[i]>max:
            max=L[i]
    return(max)

def KQ(max):
    print("phan tu lon nhat",max)

L,n=Input()
max=Search(L)
KQ(max)