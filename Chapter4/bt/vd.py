def InDaySo(n,m,k):
    for i in range(1,n+1):
        for j in range(m,k+1):
            print(j,end=", ")
        print()

InDaySo(5,1,10)