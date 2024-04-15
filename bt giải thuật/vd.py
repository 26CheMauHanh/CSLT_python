arr = []
n = int(input("Nhap so phan tu trong mang: "))

for i in range(n):
    print("Nhap phan tu ", i ,end=": ")
    a = int(input())
    arr.append(a)
for i in range(n):
        print(arr[i], " ", arr[i],"\n")