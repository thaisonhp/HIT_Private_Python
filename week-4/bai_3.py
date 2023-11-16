import re


chuoi = input("Nhap chuoi : ")
numbers = re.findall(r'-?\d+\.?\d*',chuoi)
numbers2 = [int(num) for num in numbers]
print(sum(numbers2))