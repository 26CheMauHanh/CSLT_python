n=int(input())
L=[]
for i in range(1,n+1):
    str=input()
    L=L+[str]

tbc=0
if str in L:
    str.isnumeric()
    tbc=(tbc+str(L)/str)
    
print(round(tbc,2))




    
