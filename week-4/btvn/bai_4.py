n = int(input("Nhap vao số lượng số : "))
chan = []
le = [] 
for i in range(n): 
    x = int(input("nhap so:"))
    chan.append(x) if x % 2 == 0 else le.append(x)
if sum(le) > sum(chan):
    print("odd")
elif sum(le) < sum(chan):
    print("even")
else:
    print("equal")