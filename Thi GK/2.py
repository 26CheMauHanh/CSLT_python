n=int(input())
t=0
j=0
for i in range(1,n+1):
    t=t+i
    if i%2==0:
        j=j+i
print(t-j)