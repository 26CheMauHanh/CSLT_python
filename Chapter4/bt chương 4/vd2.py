import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c

def giaipt(a,b,c):
    if a==0:
        if b==0:
            print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co mot nghiem","x=",(-c/b),end="")
            return
        
    delta=b*b-4*a*c
    z=math.sqrt(delta)
    if delta>0:
        x1=float((-b+z)/(2*a))
        x2=float((-b-z)/(2*a))
        print("Phuong trinh co hai nghiem","x1=",x1,"x2=",x2,end="")
    elif delta==0:
        x1=x2(-b/(2*a))
        print("Phuong trinh co nghiem kep","x1=x2",x1,end="")
    else:
        print("Phuong trinh vo nghiem")
    return delta

def inkq(x1,x2):
    print("Phuong trinh co hai nghiem","x1=",x1,"x2=",x2,end="")
    print("Phuong trinh co nghiem kep","x1=x2",x1,end="")

a,b,c=nhap()
delta=giaipt(a,b,c)
inkq(a,b,c,delta)