while True:
    n=int(input())
    if n>=0:
        gt=1
        for i in range(1,n+1):
            gt=gt*i
        print(gt)
    elif n<0:
        break