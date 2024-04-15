def Nhap():
    n=int(input("n="))
    return n

def Giaithua(n):
    gt=1
    for i in range(1,n+1,1):
        gt=gt*i
    return gt

def InKQ(n,gt):
    print(n,"!=",gt,sep="")

n=Nhap()
gt=Giaithua(n)
InKQ(n,gt)