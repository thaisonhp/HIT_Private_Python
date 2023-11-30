from functools import reduce
def UCLN(a,b):
    while a:
        r = b % a 
        b = a 
        a = r 
    return b

def tinhtoan(list_tu,list_mau):
    tu = reduce(lambda x, y: x * y, list_tu) 
    mau = reduce(lambda x, y: x * y, list_mau)
    new_tu = tu / (UCLN(tu,mau))
    new_mau = mau / (UCLN(tu,mau))
    return  int(new_tu) , int(new_mau)

list_tu = []
list_mau = []
n = int(input())
while n:
    x,y = list(map(int,input().split()))
    list_tu.append(x)
    list_mau.append(y)
    n -= 1
x , y = tinhtoan(list_tu=list_tu,list_mau=list_mau)
print(x,y)