#Viết chương trình:
#-Cho phép nhập vào một chuỗi là các số nhị phân 4 chữ số, phân tách bởi dấu phẩy;
#-Chương trình kiểm tra xem các số nhị phân trên có chia hết cho 3không.
#-In lên màn hình dãy số nhị phân chia hết cho 3, nếu có nhiều số thì mỗi số cách nhau bởi 1 dấu phẩy.
#TEST1:Input:0110,0010,1001,1010                #TEST2:Input:0100,0010,1010,1000
#Output:0110,1001                               #Output:
g=[]
x=input().split(',')
for i in x:
    inti=int(i,2)
    if not inti%3:
        g.append(i)
print(','.join(g))
