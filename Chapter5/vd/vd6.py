#duyệt các phần tử trong List
students=["An","Binh","Lan","Thanh","Minh"]
#cách 1
for x in students:
    print(x,end=",")

#cách 2
for x in range(len(students)):
    print(students[x],end=",")





#index() method
myPets=['Zophie','Pooka','Fat-tail']
namePet="Fat-tail"
if namePet in myPets:
    print("Iendex is", myPets.index(namePet))
else:
    print("Not Found")







#append(x) thêm phần tử x vào cuối List
#insert(i,x) chèn x vào vị trí i hiện có trong List
names=[1,2,3,4,5,6]
names.append(6)
print(names)
names.insert(0,7)
print(names)
names.insert(-1,8)
print(names)






#remove() method: xóa phần tử x đầu tiên tìm thấy trong List
#phân biệt hàm del(), remove()
#-hàm del() xóa 1 phần tử "khi biết index"
#-hàm remove() xóa 1 phần tử "khi biết giá trị"

#cách 1:
spam=['cat','bat','rat','elephant']
del(spam[1])
print(spam)

#cách 2:
spam=['cat','bat','rat','elephant']
spam.remove('bat')
print(spam)









#sort() method: cho phép sắp xếp các phần tử trong List có thứ tự
#mặc định sắp xếp tăng dần, thêm tham số reverse=True để sắp xếp giảm dần
#Lưu ý:
#-hàm sort() chỉ thực hiện được khi các phần tử có cùng kiểu dữ liệu
#-dữ liệu chuỗi sẽ đc sắp xếp theo thứ tự chữ thường trc, chữ hoa sau; a->z
n=[1,2,3,4,5]
n.sort()
print(n)
n.sort(reverse=True)
print(n)







#reverse() method: thực hiện đảo ngược thứ tự các phần tử trong List
L=["Binh","An","Nam","Anh","A"]
L.sort()
print(L)

L.reverse()
print(L)








#clear()method: thực hiện xóa tất cả các phần tử trong List

n=[1,2,3,4,5]
print(n)

n.clear()
print(n)






#count(): thực hiện đếm số phần tử x xuất hiện trong List
n=[1,2,3,2,5]
print(n.count(2))
print(n.count(5))
print(n.count(10))



#copy()method: thực hiện tạo ra 1 bản sao mới của List
n1=[1,2,3,4,5]
n2=n1.copy()
print(n1)
print(n2)

#vd khác:
names=["An","Nam","Binh","Ngoc"]
x=names.copy()
print(x)
print(x.count("Nam"))