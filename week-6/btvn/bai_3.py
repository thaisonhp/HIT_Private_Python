def tong(x,list):
    """Hàm này để tính tổng từ 1 đến x"""
    return sum(list[0:x+1:1])

n = int(input())
mang = list(map(int,input().split()))
t = int(input())
res= []
while t: 
    x = int(input())
    res.append(tong(x,mang))
    t -= 1 
for i in res : 
    print(i)