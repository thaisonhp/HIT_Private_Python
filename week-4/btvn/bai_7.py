list_input = [i for i in input().split()]
n = int(input())
list_res = []
step = int(len(list_input)/n)
for i in range(0,len(list_input),step):
    x = []
    for j in range(i,i+step):
        x.append(list_input[j])
    list_res.append(x)
print(list_res)
