n=int(input())
i=1
j=""
while i<=50:
    if (i%10)==0:
        j=j+ str(i)+"\n"
    else:
        j=j+str(i)+" "
    if i==n:
        break
    i=i+1
print("\n", j)