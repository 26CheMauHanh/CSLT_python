def Nhap():
    n=int(input("n="))
    return n

def InKQ(n):
    for i in range(2,n+1,2):
        print(i,end=" ")
    print("\nTiep tuc khong?",end="")
    kt=input()
    a="K"
    b="k"
    if kt==a or kt==b:
        None
    else:
        n=Nhap()
        InKQ(n)
        
n=Nhap()
InKQ(n)