KW=110
tien=68750.0
VAT=0.1
if 1<=KW<=100:
    gia = 550
if 101<=KW<=150:
    gia = 750
if 151<=KW<=200:
    gia = 950
if KW>201:
    gia = 1350
print("So tien ma ho gia dinh phai tra: ", KW * gia + VAT)