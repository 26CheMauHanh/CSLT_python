x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
a=("+")
b=("-")
c=("*")
d=("/")
if ch==d and y==0:
        print("Khong hop le")
elif (ch==a) or (ch==b) or (ch==d):
     print(x,ch,y,"=",round(x+y,1),sep="")