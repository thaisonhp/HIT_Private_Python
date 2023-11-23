def take_second(elemt):
    return elemt[1]
paragraph =tuple(input("Nhap doan van").split())
check = set(paragraph)
res_tuple = tuple(sorted(tuple((i,paragraph.count(i)) for i in check), key = take_second,reverse= True))
finall_tuple = tuple(i for i in res_tuple if take_second(i) == take_second(res_tuple[0]))
print(finall_tuple)
