import math
def Nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c): 
    d=b*b-4*a*c
    if d<0:
        #Phuong trinh vo nghiem
        x2=x1=None
    elif d ==0:
        #Phuong trinh co nghiem kep
        x1=x2=(-b/2*a)
    else:
        #Phuong trinh co hai nghiem
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
    return x1,x2
def Inkq(x1,x2):
    if x1==x2!=None:
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x2,sep="")
    elif x1!=x2:
        print("Phuong trinh co hai nghiem")
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")
    else:
        print("Phuong trinh vo nghiem")
a,b,c=Nhap()
x1,x2=giaipt(a,b,c)
Inkq(x1,x2)