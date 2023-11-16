n = input("so luong so ma Nasus co: ")
list_check = [1,3,5,7,9]
list_res = [] 
list_so = list(int(i) for i in input("Nhap cac so do : ").split())
for i in list_so:
    if i % 10 in list_check :
        list_res.append(i)
list_res.sort()
print("cac so ma thay Ba thich la: ")
for i in list_res:
    print(i,end=" ")