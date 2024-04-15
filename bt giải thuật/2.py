#Giải phương trình bậc 1
a=int(input("a="))
b=int(input("b="))
if a!=0:
    print("phuong trinh co nghiem x=",-b/a)
elif a==0:
    if b==0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")