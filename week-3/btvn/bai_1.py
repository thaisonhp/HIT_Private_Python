import math

print("Nhap toa do cua diem 1: ")
x1 = int(input("x1 = :"))
y1 = int(input("y1 = :"))
print("Nhap toa do cua diem 2: ")
x2 = int(input("x2 = :"))
y2 = int(input("y2 = :"))
print("Nhap toa do cua diem 3: ")
x3 = int(input("x3 = :"))
y3 = int(input("y3 = :"))
#vector AB
AB = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
# vector BC 
BC = ((x3 - x2)**2 + (y3 - y2)**2)**(1/2)
#vector AC
AC = ((x3 - x1)**2 + (y3 - y1)**2)**(1/2)
if AB + AC > BC and AB + BC > AC and BC + AC > AB:
    print("TAM GIÁC")
else:
    print("KHÔNG PHẢI TAM GIÁC")
# bài 2 

