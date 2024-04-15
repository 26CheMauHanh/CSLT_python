n=int(input("n="))
L=[]
for i in range(1,n+1):
    x=int(input())
    s=sorted(L)
    L=L+[x]
M=[]
M=M+s
print(M)
