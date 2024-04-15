#Viết chương trình:
#-Nhập vào một chuỗi gồm các từ được phân tách bởi dấu phẩy;
#-Chương trìnhthực hiệnloại bỏ các từ trùng lắp,sau đó sắp xếp các từ theo thứ tự bảng chữ cái, phân tách nhau bởi dấu phẩy rồi in kết quả ra màn hình.
#Input: without,hello,bag,world,bag,hello
#Output: bag,hello,without,world
str=input()
l=str.split(",")
x=set(l)
s=sorted(x)
print(",".join(x))