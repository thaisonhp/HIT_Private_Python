k = int(input("Nhập k: "))

for index in range(k):
    name = input("Tên:")
    point_1 = int(input("Điểm 1:"))
    point_2 = int(input("Điểm 2:"))
    res = point_1 + point_2 
    certification = 'không'
    if res >= 190:
        certification = 'XUẤT SẮC'
    elif res >= 150 and res <= 190: 
        certification = "GIỎI"
    elif res >= 100 and res <= 150 : 
        certification = "KHÁ"
    else:
        certification = "YẾU"
    print(index + 1, name , res , certification)
