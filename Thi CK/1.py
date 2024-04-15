def Input():
    n=int(input())
    L=[]
    for i in range(1,n+1):
        str=input()
        L=L+[str]
    return L

def TBC(L):
    tbc=0
    if L.isnumeric():
        tbc=tbc/L
    return tbc

def InKQ(L,tbc):
    print(round(tbc,2))

L=Input()
tbc=TBC(L)
InKQ(L,tbc)
