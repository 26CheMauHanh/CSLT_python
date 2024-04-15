S=[]
n=int(input())
m=int(input())
for i in range(n):
    S.append(0)
def Inchuoi(S,i,n,m):
    for j in range(0,m):
        S[i]=j
        if i==n-1:
            print(S)
        else:
            Inchuoi(S,i+1,n,m)
Inchuoi(S,0,n,m)