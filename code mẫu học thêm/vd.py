def Nhiphan(A,n,x):
    left=0
    right = n-1
    while left<=right:
        mid = (left+right)//2
        if x==A[mid]:
            return mid
        if x<A[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1 #Khong co trong day
A=[3,5,4,2,6,7,9,8]
n=len(A)
x=4
vitri=Nhiphan(A,n,x)
if vitri==-1:
    print( "Khong ton tai",x,"trong A")
else:
    print("Vi tri cua", x,"trong A la", vitri)