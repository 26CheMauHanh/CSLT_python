#Cho 1 danh sách và 1 từ, viết ct để chèn 1 phần tử vào trc mỗi phần tử của danh sách.
#INPUT: nhập vào dòng thứ 1 là 1 dãy các từ, mỗi từ cách nhau đúng 1 kí tự trắng. Dòng 2 là 1 từ.
#OUTPUT: in lên màn hình 1 danh sách mới gồm các phần tử chung từ 2 danh sách trên.
T=[]
st1= input()
st2=input()
K=[ ]
L=st1.split()
for i in range(len(L)):
    K=[st2]+[L[i]]
    T=T+K
print(T)