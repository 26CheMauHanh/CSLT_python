def Nhap():
    n=int(input("n="))
    L=[]
    print("Moi nhap n so nguyen:")
    for i in range(n): #range(0,n,1)
        x=int(input())
        L=L+[x]
    return L

def Dem(L):
    dem=0
    for x in L: #Duyet cac phan tu trong List
        if x%2==0:
            dem=dem+1
    return dem

def InKQ(kq):
    print("Co",kq,"so chan")

L=Nhap()
kq=Dem(L)
InKQ(kq)