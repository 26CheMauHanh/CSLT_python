#viết ct:
#cho phép nhập vào 1 chuỗi ký tự bất kỳ.
#ct thực hiện đếm có bn chữ cái in hoa, chữ cái in thường, chữ số và ký tự khác (bao gồm ký tự trắng) xuất hiện trong chuỗi trên.
#In kết quả lên màn hình.
#INPUT: Python Programming Class @2021!
#OUTPUT: In hoa: 3  /In thuong: 19   /Chu so: 4     /Khac: 5
def Dem(st):
    dem1=0 # in hoa
    dem2=0 # in thường
    dem3=0 # chữ số 
    dem4=0 # kí tự khác
    for x in st:
        if x.isupper():
            dem1=dem1+1
        elif x.islower():
            dem2=dem2+1
        elif x.isnumeric():
            dem3=dem3+1
        else:
            dem4=dem4+1
    return dem1,dem2,dem3,dem4

st=input()
dem1,dem2,dem3,dem4=Dem(st)
print("In hoa:",dem1)
print("In thuong:",dem2)
print("Chu so:",dem3)
print("Khac:",dem4)