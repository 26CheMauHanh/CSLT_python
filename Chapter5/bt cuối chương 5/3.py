#Nhập từ bàn phím một số nguyên n(n>0),và nsố nguyênlưu trữ vào một List.
#In lên màn hình: 
#-Số lượng các sốnguyên DƯƠNG
#-Trung bình cộng của các số nguyên chẵn được lưu trữ trong List trên.
#TEST:            
#n=5
#6
#2
#-1
#2
#7
#SND=3
#TBC=2.0
n=int(input("n="))
L=[]
for i in range(1,n+1):
    x=int(input())
    L=L+[x]
dem=0
for x in L:
    if x>0:
        dem=dem+1
print("SND=",dem,sep="")