yrsOfService=int(input("So nam lam viec:"))
salary=int(input("Muc luong hien tai cua nhan vien do:"))
m1=int(input("Tien thuong m1: "))
m2=int(input("Tien thuong m2: "))
m3=int(input("Tien thuong m3: "))
bonus=0
if yrsOfService < 5:
    if salary < 500:
        bunus = m1
    else:
        bonus = m2
else:
    bonus = m3
print("Tien thuong cua nhan vien: ", bonus)