n=int(input("n="))
i=1
while i<=n:
    k=1
    while k<=(n-i):
        print(" ",end="")
        k=k+1
    j=1
    while j<=(2*i-1):
        print("*",end="")
        j=j+1
    print()
    i=i+1