#Tính n! với 0!=1, n!=n*(n-1)*(n-2)…1
n=int(input("n="))
if n>=0:
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    print(n,"!=",gt,sep="")
elif n<0:
    None