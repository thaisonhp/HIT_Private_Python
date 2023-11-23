my_list_a = list(i for i in input().split())
my_tuple_b = tuple(i for i in my_list_a)
count_number_in_b = 0 
for i in my_tuple_b: 
    if i.isnumeric():
        count_number_in_b += 1 
print(count_number_in_b)