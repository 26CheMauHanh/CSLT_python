#trả về chiều dài của List
s=[1,2,3,4,5,6]
len(s)
print(len(s))

m=[[1,2,3],[4,5,6],[7,8,9]]
len(m)
print(len(m))
len(m[0])
print(len(m[0]))




#giá trị lớn nhất, nhỏ nhất
n=[5,3,8,2,9]
print(max(n))
print(min(n))





#xóa phần tử trong list với hàm del()
spam=[1,2,3,4,5]
del(spam[2])
print(spam)

del(spam[1])
print(spam)




#xóa phần tử trong List với hàm del()
students=["An","Binh","Lan","Thanh","Minh"]
del(students[2])
print(students)

del(students[1])
del(students[2])
print(students)