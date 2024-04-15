x=float(input("x="))
y=float(input("y="))
a=("+")
b=("-")
c=("*")
d=("/")
ch=input("Phep toan:")
if ch==d:
    if y==0:
        print("Khong hop le")
elif ch==a or ch==b or ch==c or ch==d:
    print(x, "+", y, "=",round((x+y),1),sep="")
else:
    print("Khong hop le")