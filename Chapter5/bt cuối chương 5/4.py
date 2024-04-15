#Nhập từ bàn phím một số nguyên n(n>0)và n số nguyên lưu vào List A:
#-Hãy đảo ngược giá trị của các phần tử trong List A và lưu vào List B.
#In giá trị các phần tử trong List B sau khi thực hiện đảo;
#-Sắp xếp và in lên màn hình List B sau khi được sắp xếp tăng dần;
#TEST:
#n=5
#3
#1
#4
#2
#5
#[5,2,4,1,3]
#[1,2,3,4,5]
n=int(input("n="))
A=[]
for i in range(1,n+1):
    x=int(input())
    A=A+[x]
A.reverse()
print(A)
A.sort()
print(A)