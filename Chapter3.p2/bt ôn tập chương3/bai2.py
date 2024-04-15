n=int(input("n="))
if n<2:
    print(n, "khong la SNT")
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,"khong la SNT")
            break
    else:
        print(n,"la SNT")