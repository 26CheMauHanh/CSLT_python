#phép tham chiếu(References)
#phép gán trong biến đơn
spam=[0,1,2,3,4,5]
cheese=spam
cheese[1]='Hello'
print(spam)






#vd 
import copy
n1=[1,2,3,4,5]
n2=copy.copy(n1)
print(n2)

n3=n1
n3[2]=6
print(n3)