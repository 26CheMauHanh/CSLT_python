def tinh_tich(n):
    if (n == 1):
        return 1
    return n * tinh_tich(n-1)
print("Hãy nhập vào số n: ")
n = int(input())
tich = tinh_tich(n)
print("Tich là: ", tich)