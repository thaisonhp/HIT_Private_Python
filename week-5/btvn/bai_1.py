table_1 = set(i for i in input("Nhap ma sinh vien dang ki ban 1: ").split())
table_2 = set(i for i in input("Nhap ma sinh vien dang ki ban 2: ").split() )
if table_1 & table_2:
    print("Danh sach sanh vien dang ky o hai ban la: ",table_2&table_1)
else:
    print("Khong co sinh vien nao dang ky o hai ban.")
print("Danh sach sinh vien dang ky o hai ban la: ", table_1 | table_2)
print("Danh sach sinh vien dang ky ban 1 ma khong dang ki ban 2 la :", table_1 - table_2)
print("Danh sach sinh vien chi dang ky o 1 trong 2 ban la:" , table_1 ^ table_2)
