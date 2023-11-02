

# note : print(*object, sep = '',end = '\n', file = sys.stdout , flush = False)
# độ
# src = open("text.txt",'w')
# print("Posiden Tien" , file = src)
a = 10
res = []
while int(a) > 0:
    r = int(a % 2)
    res.append(r)
    a /= 2
print(res)