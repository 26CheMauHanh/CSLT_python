a=float(input())
b=float(input())
c=float(input())
DTB=(a*2+b*3+c)/6
if DTB<3:
    print("Kem")
elif 3<=DTB<5:
    print("Yeu")
elif 5<=DTB<6:
    print("Trung binh")
elif 6<=DTB<7:
    print("Trung binh Kha")
elif 7<=DTB<8:
    print("Kha")
elif 8<=DTB<9:
    print("Gioi")
else:
    print("Xuat sac")