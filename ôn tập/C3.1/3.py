x=float(input("x="))
y=float(input("y="))
ck=input("Phep toan:")
if ck=="+" or ck=="-" or ck=="*" or ck=="/":
    print(x,"+",y,"=",round((x+y),1),sep="")
    if ck=="/" and y==0:
        print("Khong hop le")
else:
    print("Khong hop le")