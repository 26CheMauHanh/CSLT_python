n=int(input())
S=[]
for i in range(n):
    S.append(0)
def Inchuoi(s,i,n):
    for j in range(0,2):
        S[i]=j
        if i==n-1:
            print(S)
        else:
            Inchuoi(S,i+1,n)
Inchuoi(S,0,n)