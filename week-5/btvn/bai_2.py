n = int(input("Nhap vao so phan tu cua set:"))
father_set = (int(i) for i in input().split())
father_set_fake = sorted(father_set)
k = int(input("Nhap vao so k: "))
test = k
res_set = set()
if test < father_set_fake[0]:
    print("Khong co set con nao thoa man!")
else:
    for i in father_set_fake:
        test -= i 
        if test < 0:
            break
        res_set.add(i)
print(res_set)