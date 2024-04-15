def nhap():
    n=int(input("n="))
    return n

def inkq(n):
    for i in range(2,n+1,2):
        print(i,end=" ")
    print("\nCo tiep tuc khong?",end="")
    a=input()
    if a=="K" or a=="k":
        print()
    else: 
        n=nhap()
        inkq(n)

n=nhap()
inkq(n)
