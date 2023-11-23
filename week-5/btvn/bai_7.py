string_input = tuple(input("Nhap vao chuoi:"))
dict_res = {}
for i in string_input:
    if i not in dict_res:
        dict_res[i] = 1
    else:
        dict_res[i] += 1
print(dict_res)