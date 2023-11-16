list_bandau = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
list_res = []
for i in list_bandau:
    if isinstance(i,list):
        for j in i : 
            list_res.append(j)
    else:
        list_res.append(i)
print(list_res)
