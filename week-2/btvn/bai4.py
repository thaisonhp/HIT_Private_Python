a = float(input("Nhap so a:"))
if(a == int(a)): # nếu a là số nguyên 
    res = []
    while int(a) > 0 : 
        r = int(a % 2) 
        res.append(r)
        a /= 2 
    res.reverse()
    print(res)
    if res[0] == 0:
        print("số lượng bit cần là: " , len(res) - 1)
    else: 
        print("Số lượng bit cần là: " , len(res))
else: # nếu a là số thực
    interger_part = int(a)
    print(interger_part)
    decimal_part = a - int(a)
    print(decimal_part)
    # đổi phần số nguyên
    bit_interger = []
    while int(interger_part) > 0 : 
        r = int(interger_part % 2) 
        bit_interger.append(r)
        interger_part /= 2 
    bit_interger.reverse()
    # đổi phần thập phân
    check = []
    bit_decimal = []
    while decimal_part != 1.0 : 
        if decimal_part in check : 
            bit_decimal.append(int(decimal_part))
            break; 
        else:
            check.append(decimal_part)
            bit_decimal.append(int(decimal_part*2))
            decimal_part = decimal_part*2 - int(decimal_part*2)
    # xử lý phần số 0 dư ra
    bit_decimal.reverse()
    for i in range(0,len(bit_decimal)):
        if bit_decimal[i] == 1 :
            new_bit_decimal = bit_decimal[i:]
            break
    new_bit_decimal.reverse()
for i in bit_interger:
    print(i,end = " ")
print(".", end="")
for i in new_bit_decimal:
    print(i,end=" ")
print('Tong so bit can de luu tru la:' ,len(bit_interger) + len(bit_decimal))


# ý b 
# a = 10 
# print(dir(a))