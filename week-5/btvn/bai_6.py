my_dict = {}
index = 1
print("Mời bạn nhập:")
check = "YES"
while check == "YES":
    msv = input(f"Moi ban nhap msv cua sinh vien thu {index} !")
    overall_point = float(input(f"Moi ban nhap ma sinh vien cua sinh vien thu {index}:"))
    my_dict[msv] = overall_point 
    check = input("Ban co muon nhap nua hay khong!(YES/NO)")
    index += 1
check_overall_point = 0 
for i in my_dict:
    if my_dict[i] >= 2.5 and my_dict[i] <= 3.5:
        check_overall_point += 1
msv = input("Nhap ma sinh vien cua sinh vien muon bo sung:")
overall_point = float(input("Nhap diem tong ket cua sinh vien nay:"))
my_dict[msv] = overall_point
for i in my_dict:
    if my_dict[i] < 2.0 : 
        my_dict.pop(i)
print("Tu dien sau khi xoa la:",my_dict)



