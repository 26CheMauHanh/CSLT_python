n=int(input()) 
while n>=0:
    gt=1
    i=1
    while i<=n:
        if n==0:
            continue
        else:
            gt=gt*i
        i=i+1
    print(gt)
    n=int(input())
    if n<0:
        break