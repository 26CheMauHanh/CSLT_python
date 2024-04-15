#In ra tất cả các số hoàn hảo từ 1 đến n
#a=0 không phải là số hoàn hảo
#a=1 số hoàn hảo
def kt(n):
    a=0
    u=[i for i in range(1,n) if n%i==0 ]
    
    s=0
    for i in range(len(u)):
        s+=u[i]
        
    if s==n:
        a=1
    return a

n=int(input("n="))

for i in range(n):
    x=kt(i)
    if x==1:
        print(i)
