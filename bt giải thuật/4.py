#In ra tất cả các số nguyên tố từ 1 đến n
#a=0 không phải số nguyên tố
#a=1 #số nguyên tố
def kt(n):
    a=1
    if n<2:
        a=0
        return a
        
    for i in range(2,n):
        if n%i==0:
            a=0
            break
    return a
n=int(input("n="))
for s in range(n):
    x=kt(s)
    if x==1:
        print(s)
