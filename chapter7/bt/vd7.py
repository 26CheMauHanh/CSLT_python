#Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com,
#hãy viết một chương trình để in username của địa chỉ email cụ thể.
# Cả username và companyname chỉ bao gồm chữ cái.

#Ví dụ: Nếu cung cấp địa chỉ email QTM@quantrimang.com thì đầu ra sẽ là: QTM.

#Trong trường hợp dữ liệu đầu vào không có sẵn, ta giả định nó được người dùng nhập vào từ giao diện điều khiển.
import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
re2 = re.match(pat2,emailAddress)
print (re2.group(1)) 

#nếu đầu ra là: quantrimang
import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print (r2.group(2))