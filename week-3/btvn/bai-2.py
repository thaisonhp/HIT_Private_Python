m = int(input("Nhập m: "))
n = int(input("Nhập n:"))
# while n: 
#     x = input("Nhập số nhiều hơn 6 chữ số: ")
#     last_x = x[-1:-1-m:-1]
#     first_x = x[0:len(x)-m:]
#     print(first_x+last_x)
#     n -= 1
for i in range(n):
    x = input("Nhập số nhiều hơn 6 chữ số: ")
    last_x = x[-1:-1-m:-1]
    first_x = x[0:len(x)-m:]
    print(first_x+last_x)
