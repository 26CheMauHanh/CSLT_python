A=[1,2,3,4,5,6,3,5,6,2]
n=len(A)
x=2
def LinearSearch(A,n,x):
    left=0
    right=n-1
    while (left<=right):
        mid=(left+right)//2
        if (x==A[mid]):
            return mid
        if (x<A[mid]):
            right=mid-1
        else:
            left=mid+1
    return -1;
