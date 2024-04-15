#1.Capitalize(): td in hoa chữ cái đầu tiên của chuỗi
str="hoctap"
str1=str.capitalize()
print(str1)
#kq: Hoctap


#2.Center(): td trả về chuỗi đc hiển thị ở giữa 1 chuỗi
#cú pháp: str.center(len,char)    
#len: số lượng ký tự của chuỗi mới
#char: ký tự sẽ hiển thị ở 2 bên chuỗi. mặc định nó sẽ là khoảng trắng
str="hoctap"
str1=str.center(10,'*')
print(str1)
#kq: **hoctap**


#3.count(): td đếm xem trong chuỗi có bn ký tự cần tìm
#cú pháp: str.count(sub,start,end)
#sub: là chuỗi cần tìm
#start: là index bắt đầu. mặc định thì start=0
#end: là index kết thúc. mặc định thì end=len() của chuỗi
str="hoctap"
print(str.count('h',3))
#kq: 1


#4.endswith(): td kt xem chuỗi hoặc khoảng chuỗi có đc kết thúc bằng ký tự nào đó hay ko. nó sẽ trả về True nếu đúng và False nếu sai
#cú pháp: str.endswith(str,start,end)
#str: chuỗi cần kết thúc
#start: index bắt đầu. md start=0
#end: index kết thúc
str="hoctap"
print(str.endswith('p'))
#kq: True


#5.expandtabs(): td tìm kiếm thay thế \t bằng các ký tự trắng
str="hoctap\hc lap trinh"
print(str.expandtabs())
#kq: hoctap     hc lap trinh


#6.isalnum(): td kiểm tra 1 chuỗi chỉ chứa các ký tự chữ hoặc số.
str="hoctap123"
print(str.isalnum())
#kq: True


#7.isalpha(): td kiểm tra 1 chuỗi chỉ chứa các ký tự chữ cái.


#8.isdigit(): hàm chỉ chứa chữ số


#9.islower(): td kiểm tra 1 chuỗi có phải là in thường hay ko
#10.lower(): chuyển đổi về dạng in thường

#11.isupper(): td kiểm tra 1 chuỗi có phải là in Hoa hay ko.
#12.upper(): chuyển đổi về dạng in hoa

#13.isnumeric(): td kt 1 chuỗi chỉ chứa duy nhất các ký tự số hay ko.


#14.isspace():kt 1 chuỗi có phải chỉ chứa các ký tự khoảng trắng ko.


#15.istitle(): kt 1 chuỗi có các chữ cái đầu đều đc in hoa.
str="hoc tap"
print(str.istitle())
#kq: Hoc Tap
#16.title(): chuyển đổi chữ cái đầu đều được in hoa.


#17.join(): dùng để nối chuỗi với nhau
str1='-'
str2=['H','A','H']
print(str1.join(str2))
#kq: H-A-H


#18.len(): td trả về độ dài của chuỗi
str="hoc tap"
print(len(str))
#kq: 7  (tính luôn cả khoảng trắng)


#19.ljust(): td trả về 1 chuỗi với độ dài đc xác định, được bù về phía bên phải của chuỗi
str="hoc tap"
print(str.ljust(10,"-"))
#kq: hoc tap---


#20.rjust(): được bù về phía bên trái của chuỗi.


#21.lstrip(): loại bỏ các ký tự ở phía đầu của chuỗi
str="---hc tap"
print(str.lstrip('-'))
#kq: hc tap


#22.rstrip(): loại bỏ các ký tự ở phía cuối của chuỗi


#23.strip(): loại bỏ ở cả 2 đầu


#24.replace():td tìm kiếm và thay thế chuỗi tìm được bằng chuỗi mới
#cú pháp: str.replace(old,new,max)
#old: chuỗi cần tìm
#new: chuỗi cần thay thế
#max: số lượng thay thế tối đa
str=="A A A"
print(str.replace('A', 'Tai',2))
#kq: Tai Tai A


#25.max():hàm trả về chữ cái có độ sắp xếp cuối cùng theo bảng chữ cái alphabet nằm trong chuỗi
str="a b c k"
print(max(str))
#kq: k


#26.min():hàm trả về chữ cái có độ sắp xếp đầu tiên theo bảng chữ cái alphabet nằm trong chuỗi


#27.swapcase(): chuyển đổi chuỗi sang dạng nghịch đảo của nó(hoa sang thường)
str="hoc tap"
print(str.swapcase())
#kq: Hoc Tap


#28.split(): td tách chuỗi thành mảng 
#cú pháp: str.split(char,max)
str="hoc tap"
print(str.split())
#kq: ['hoc', 'tap']


#29.del():  hàm để xóa phần tử trong list khi biết "index"
st=['An','Binh','Lan','Minh']
del(st[2])
print(st)
#kq: ['An','Binh', 'Minh']
#30.remove(): xóa phần tử trong list khi biết "giá trị"
st=['An','Binh','Lan','Minh']
st.remove('An')
print(st)
#kq: ['Binh','Lan','Minh']



#31.append(x): thêm phần tử x vào cuối List
st=[1,2,3,4,5,6]
st.append(6)
print(st)
#kq: [1,2,3,4,5,6,6]


#32.insert(i,x): chèn x vào vị trí i hiện có trong List
st=[1,2,3,4,5,6]
st.insert(0,7)
print(st)
#kq: [7,1,2,3,4,5,6]


#33.sort(): sắp xếp các phần tử trong List có thứ tự tăng dần. nếu xếp giảm dần, thêm tham số "reverse=True"
st=['c','d','a']
st.sort()
print(st)
#kq: ['a','c','d']

#34.reverse(): đảo ngược thứ tự trong List

#35.clear():xóa tất cả các phần tử trong list

#36.pop(i): xóa và lấy ra giá trị của phần tử có số chỉ mục i trong list
n=[1,2,3,4,5]
x=n.pop(2)
print(n)
print(x)
#kq: [1,2,4,5]
#    3



#hàm set(): xóa phần tử trùng lặp mà ko giữ thứ tự list ban đầu
#hàm sorted(): xóa phần tử trùng lặp và giữ nguyên thứ tự list ban đầu