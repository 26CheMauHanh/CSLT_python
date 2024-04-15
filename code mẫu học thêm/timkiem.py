A=[1,2,3,4,5,6,3,5,6,2]
n=len(A)
x=2
def LinearSearch(A,n,x):
    A=A+[x] #A.append(x)
    i=0
    while A[i]!=x:
        i=i+1
    return i

vitri=LinearSearch(A,n,x)
if vitri ==n:
    print("Khong ton tai",x,"trong A")
else:
    print("vi tri cua",x,"trong A la",vitri)