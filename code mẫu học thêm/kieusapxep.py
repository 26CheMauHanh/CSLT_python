# interchange sort: kiểu đổi chỗ trực tiếp
def interchangeSort(m):
    for i in range(0,len(m)-1):
        for j in range(i+1,len(m)):
            if m[j]< m[i]:
                #hoán đổi vị trí
                t=m[i]
                m[i]=m[j]
                m[j]=t
m=[3,45,2,43,5,25,65,8,57,67]
interchangeSort(m)
print(m)