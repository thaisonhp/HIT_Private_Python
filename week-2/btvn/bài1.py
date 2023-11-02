# câu 1 
a  = 10 
b = 3
print(a + b) 
print(a - b) 
print(a*b)
print(a**b)
print(a > b) 
print(a < b) 
print(a == b)
print(a and b)
print(a or b)
print(a ^ b) # a xor b 
print(not(a ==b))
print(~10)
print(a >> 5)
print(a << 6)
res = []
while int(a) > 0:
    r = int(a % 2)
    res.append(r)
    a /= 2
for i in res:
    print(i,end = " ")
