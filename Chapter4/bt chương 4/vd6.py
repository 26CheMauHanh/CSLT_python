def Nhap():
    n=int(input("n="))
    return n
def InKQ(n):
    while True:
        for i in range (1,n+1):
            if i%2==0:
                print(i," ",end="")
        m=input("\nTiep tuc khong?")
        if m=="K" or m=="k":
           break      
        if m=="t":
           continue
n= Nhap()
InKQ(n)