def fibonacci_phi_de_quy(n):
    f0 = 0
    f1 = 1
    fn = 1

    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn


def fibonacci_de_quy(n):
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


n = int(input('Nhap vao so nguyen duong n = '))
print(n, ' so dau tien cua day Fibonacci la:')
for i in range(0, n):
    print(fibonacci_phi_de_quy(i), " - ", fibonacci_de_quy(i))
