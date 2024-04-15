#pop(i): thực hiện "xóa và lấy ra giá trị của phần tử" có số chỉ mục i trong List
#nếu tham số i để trống thì mặc định là "lấy phần tử cuối" trong List
n=[1,2,3,4,5]
x=n.pop(2)
print(n)
print(x)

#vd khác
n=[1,2,3,4,5]
x=n.pop()
print(n)
print(x)





#vd khác
names=["An","Nam","Binh","Ngoc"]
x1=names.pop(0)
x2=names.pop(-1)
print(x1)
print(x2)
print(names)



#vd khác
names=["An","Nam","Binh","Ngoc"]
names.remove("An")
del(names[0])
x=names.pop(-2)
print(x)
print(names)