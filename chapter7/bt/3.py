#. Bạn hãy viết chương trình để thực hiện kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào. Biết rằng, chính sách mật khẩu được quy định như sau:
#-Ít nhất 1 chữ cái nằm trong [a-z]
#-Ít nhất 1 số nằm trong [0-9]
#-Ít nhất 1 kí tự nằm trong [A-Z]
#-Ít nhất 1 ký tự nằm trong [$ # @]
#-Độ dài mật khẩu tối thiểu: 6 ký tự
#-Độ dài mật khẩu tối đa: 17 ký tự
#Trong đó,Inputlà một chuỗi ký tự được đặt làm mật khẩu, OutputlàTruenếu hợp lệ, còn lại là False.
#TEST1:Input:ChucQuaMon@2021               #TEST2:Input:IAmFine
#Output:True                               #Output:False
import re
b=input()
def kiemtra(b):
    if 6<len(b)<17:
        
            if  re.search("[a-z]",b):
                
                if  re.search("[0-9]",b):
                    
                    if  re.search("[A-Z]",b):
                        
                        if  re.search("[$#@]",b):
                            
                            
                                return True 
                            # else: return False
                        else:return False
                    else:return False
                else:return False
            else:return False
    else:
        return False
print(kiemtra(b))