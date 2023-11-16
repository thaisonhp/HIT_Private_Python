list_ban_dau = [i for i in input().split()]
dic_check = {}
for i in list_ban_dau:
    if i in dic_check:
        dic_check[i].append(i)
    else:
        dic_check[i] = list(i)
list_res = list(dic_check.values())
print(list_res)


